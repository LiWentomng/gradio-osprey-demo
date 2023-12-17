"""gr.Dropdown() component."""

from __future__ import annotations

import warnings
from typing import Any, Callable, Literal

from gradio_client.documentation import document, set_documentation_group
from gradio_client.serializing import SimpleSerializable

from gradio.components.base import FormComponent, IOComponent, _Keywords
from gradio.deprecation import warn_style_method_deprecation
from gradio.events import (
    Blurrable,
    Changeable,
    EventListenerMethod,
    Inputable,
    Selectable,
)

set_documentation_group("component")


@document()
class Dropdown(
    FormComponent,
    Changeable,
    Inputable,
    Selectable,
    Blurrable,
    IOComponent,
    SimpleSerializable,
):
    """
    Creates a dropdown of choices from which entries can be selected.
    Preprocessing: passes the value of the selected dropdown entry as a {str} or its index as an {int} into the function, depending on `type`.
    Postprocessing: expects a {str} corresponding to the value of the dropdown entry to be selected.
    Examples-format: a {str} representing the drop down value to select.
    Demos: sentence_builder, titanic_survival
    """

    def __init__(
        self,
        choices: list[str] | None = None,
        *,
        value: str | list[str] | Callable | None = None,
        type: Literal["value", "index"] = "value",
        multiselect: bool | None = None,
        max_choices: int | None = None,
        label: str | None = None,
        info: str | None = None,
        every: float | None = None,
        show_label: bool = True,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        interactive: bool | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        allow_custom_value: bool = False,
        **kwargs,
    ):
        """
        Parameters:
            choices: list of options to select from.
            value: default value(s) selected in dropdown. If None, no value is selected by default. If callable, the function will be called whenever the app loads to set the initial value of the component.
            type: Type of value to be returned by component. "value" returns the string of the choice selected, "index" returns the index of the choice selected.
            multiselect: if True, multiple choices can be selected.
            max_choices: maximum number of choices that can be selected. If None, no limit is enforced.
            label: component name in interface.
            info: additional component description.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            interactive: if True, choices in this dropdown will be selectable; if False, selection will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            allow_custom_value: If True, allows user to enter a custom value that is not in the list of choices.
        """
        self.choices = [str(choice) for choice in choices] if choices else []
        valid_types = ["value", "index"]
        if type not in valid_types:
            raise ValueError(
                f"Invalid value for parameter `type`: {type}. Please choose from one of: {valid_types}"
            )
        self.type = type
        self.multiselect = multiselect
        if multiselect and isinstance(value, str):
            value = [value]
        if not multiselect and max_choices is not None:
            warnings.warn(
                "The `max_choices` parameter is ignored when `multiselect` is False."
            )
        self.max_choices = max_choices
        self.allow_custom_value = allow_custom_value
        if multiselect and allow_custom_value:
            raise ValueError(
                "Custom values are not supported when `multiselect` is True."
            )
        self.interpret_by_tokens = False
        self.select: EventListenerMethod
        """
        Event listener for when the user selects Dropdown option.
        Uses event data gradio.SelectData to carry `value` referring to label of selected option, and `index` to refer to index.
        See EventData documentation on how to use this event data.
        """
        IOComponent.__init__(
            self,
            label=label,
            info=info,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            **kwargs,
        )

    def api_info(self) -> dict[str, dict | bool]:
        if self.multiselect:
            type = {
                "type": "array",
                "items": {"type": "string"},
                "description": f"List of options from: {self.choices}",
            }
        else:
            type = {"type": "string", "description": f"Option from: {self.choices}"}
        return {"info": type, "serialized_info": False}

    def example_inputs(self) -> dict[str, Any]:
        if self.multiselect:
            return {
                "raw": [self.choices[0]] if self.choices else [],
                "serialized": [self.choices[0]] if self.choices else [],
            }
        else:
            return {
                "raw": self.choices[0] if self.choices else None,
                "serialized": self.choices[0] if self.choices else None,
            }

    def get_config(self):
        return {
            "choices": self.choices,
            "value": self.value,
            "multiselect": self.multiselect,
            "max_choices": self.max_choices,
            "allow_custom_value": self.allow_custom_value,
            **IOComponent.get_config(self),
        }

    @staticmethod
    def update(
        value: Any | Literal[_Keywords.NO_VALUE] | None = _Keywords.NO_VALUE,
        choices: str | list[str] | None = None,
        label: str | None = None,
        info: str | None = None,
        show_label: bool | None = None,
        container: bool | None = None,
        scale: int | None = None,
        min_width: int | None = None,
        interactive: bool | None = None,
        placeholder: str | None = None,
        visible: bool | None = None,
    ):
        return {
            "choices": choices,
            "label": label,
            "info": info,
            "show_label": show_label,
            "container": container,
            "scale": scale,
            "min_width": min_width,
            "visible": visible,
            "value": value,
            "interactive": interactive,
            "placeholder": placeholder,
            "__type__": "update",
        }

    def preprocess(
        self, x: str | list[str]
    ) -> str | int | list[str] | list[int] | None:
        """
        Parameters:
            x: selected choice(s)
        Returns:
            selected choice(s) as string or index within choice list or list of string or indices
        """
        if self.type == "value":
            return x
        elif self.type == "index":
            if x is None:
                return None
            elif self.multiselect:
                return [self.choices.index(c) for c in x]
            else:
                if isinstance(x, str):
                    return self.choices.index(x) if x in self.choices else None
        else:
            raise ValueError(
                f"Unknown type: {self.type}. Please choose from: 'value', 'index'."
            )

    def set_interpret_parameters(self):
        """
        Calculates interpretation score of each choice by comparing the output against each of the outputs when alternative choices are selected.
        """
        return self

    def get_interpretation_neighbors(self, x):
        choices = list(self.choices)
        choices.remove(x)
        return choices, {}

    def get_interpretation_scores(
        self, x, neighbors, scores: list[float | None], **kwargs
    ) -> list:
        """
        Returns:
            Each value represents the interpretation score corresponding to each choice.
        """
        scores.insert(self.choices.index(x), None)
        return scores

    def style(self, *, container: bool | None = None, **kwargs):
        """
        This method is deprecated. Please set these arguments in the constructor instead.
        """
        warn_style_method_deprecation()
        if container is not None:
            self.container = container
        return self
