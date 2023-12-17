"""gr.Chatbot() component."""

from __future__ import annotations

import inspect
from pathlib import Path
from typing import Callable, Literal

from gradio_client import utils as client_utils
from gradio_client.documentation import document, set_documentation_group
from gradio_client.serializing import JSONSerializable

from gradio import utils
from gradio.components.base import IOComponent, _Keywords
from gradio.deprecation import warn_deprecation, warn_style_method_deprecation
from gradio.events import (
    Changeable,
    EventListenerMethod,
    Selectable,
)

set_documentation_group("component")


@document()
class Chatbot(Changeable, Selectable, IOComponent, JSONSerializable):
    """
    Displays a chatbot output showing both user submitted messages and responses. Supports a subset of Markdown including bold, italics, code, and images.
    Preprocessing: passes the history of messages as a {List[List[str | None | Tuple]]}, i.e. a list of lists. The inner list has 2 elements: the user message and the response message. Messages can be strings, tuples (filepath to image/video/audio, [optional string alt text]), or `None`.
    Postprocessing: expects function to return a {List[List[str | None | Tuple]]}, i.e. a list of lists. The inner list should have 2 elements: the user message and the response message. Messages should be strings, tuples, or Nones. If the message is a string, it can include Markdown. If it is a tuple, it should consist of (filepath to image/video/audio, [optional string alt text]). Messages that are `None` are not displayed.

    Demos: chatbot_simple, chatbot_multimodal
    Guides: creating-a-chatbot
    """

    def __init__(
        self,
        value: list[list[str | tuple[str] | tuple[str | Path, str] | None]]
        | Callable
        | None = None,
        color_map: dict[str, str] | None = None,
        *,
        label: str | None = None,
        every: float | None = None,
        show_label: bool = True,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        height: int | None = None,
        latex_delimiters: list[dict[str, str | bool]] | None = None,
        show_share_button: bool | None = None,
        **kwargs,
    ):
        """
        Parameters:
            value: Default value to show in chatbot. If callable, the function will be called whenever the app loads to set the initial value of the component.
            label: component name in interface.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            height: height of the component in pixels.
            latex_delimiters: A list of dicts of the form {"left": open delimiter (str), "right": close delimiter (str), "display": whether to display in newline (bool)} that will be used to render LaTeX expressions. If not provided, `latex_delimiters` is set to `[{ "left": "$$", "right": "$$", "display": True }]`, so only expressions enclosed in $$ delimiters will be rendered as LaTeX, and in a new line. Pass in an empty list to disable LaTeX rendering. For more information, see the [KaTeX documentation](https://katex.org/docs/autorender.html).
            show_share_button: If True, will show a share icon in the corner of the component that allows user to share outputs to Hugging Face Spaces Discussions. If False, icon does not appear. If set to None (default behavior), then the icon appears if this Gradio app is launched on Spaces, but not otherwise.
        """
        if color_map is not None:
            warn_deprecation("The 'color_map' parameter has been deprecated.")
        self.select: EventListenerMethod
        """
        Event listener for when the user selects message from Chatbot.
        Uses event data gradio.SelectData to carry `value` referring to text of selected message, and `index` tuple to refer to [message, participant] index.
        See EventData documentation on how to use this event data.
        """
        self.height = height
        if latex_delimiters is None:
            latex_delimiters = [{"left": "$$", "right": "$$", "display": True}]
        self.latex_delimiters = latex_delimiters
        self.show_share_button = (
            (utils.get_space() is not None)
            if show_share_button is None
            else show_share_button
        )

        IOComponent.__init__(
            self,
            label=label,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            **kwargs,
        )

    def get_config(self):
        return {
            "value": self.value,
            "latex_delimiters": self.latex_delimiters,
            "selectable": self.selectable,
            "height": self.height,
            "show_share_button": self.show_share_button,
            **IOComponent.get_config(self),
        }

    @staticmethod
    def update(
        value: list[list[str | tuple[str] | tuple[str, str] | None]]
        | Literal[_Keywords.NO_VALUE]
        | None = _Keywords.NO_VALUE,
        label: str | None = None,
        show_label: bool | None = None,
        container: bool | None = None,
        scale: int | None = None,
        min_width: int | None = None,
        visible: bool | None = None,
        height: int | None = None,
        show_share_button: bool | None = None,
    ):
        updated_config = {
            "label": label,
            "show_label": show_label,
            "container": container,
            "scale": scale,
            "min_width": min_width,
            "visible": visible,
            "value": value,
            "height": height,
            "show_share_button": show_share_button,
            "__type__": "update",
        }
        return updated_config

    def _preprocess_chat_messages(
        self, chat_message: str | dict | None
    ) -> str | tuple[str] | tuple[str, str] | None:
        if chat_message is None:
            return None
        elif isinstance(chat_message, dict):
            if chat_message["alt_text"] is not None:
                return (chat_message["name"], chat_message["alt_text"])
            else:
                return (chat_message["name"],)
        else:  # string
            return chat_message

    def preprocess(
        self,
        y: list[list[str | dict | None] | tuple[str | dict | None, str | dict | None]],
    ) -> list[list[str | tuple[str] | tuple[str, str] | None]]:
        if y is None:
            return y
        processed_messages = []
        for message_pair in y:
            assert isinstance(
                message_pair, (tuple, list)
            ), f"Expected a list of lists or list of tuples. Received: {message_pair}"
            assert (
                len(message_pair) == 2
            ), f"Expected a list of lists of length 2 or list of tuples of length 2. Received: {message_pair}"
            processed_messages.append(
                [
                    self._preprocess_chat_messages(message_pair[0]),
                    self._preprocess_chat_messages(message_pair[1]),
                ]
            )
        return processed_messages

    def _postprocess_chat_messages(
        self, chat_message: str | tuple | list | None
    ) -> str | dict | None:
        if chat_message is None:
            return None
        elif isinstance(chat_message, (tuple, list)):
            file_uri = str(chat_message[0])
            if utils.validate_url(file_uri):
                filepath = file_uri
            else:
                filepath = self.make_temp_copy_if_needed(file_uri)

            mime_type = client_utils.get_mimetype(filepath)
            return {
                "name": filepath,
                "mime_type": mime_type,
                "alt_text": chat_message[1] if len(chat_message) > 1 else None,
                "data": None,  # These last two fields are filled in by the frontend
                "is_file": True,
            }
        elif isinstance(chat_message, str):
            chat_message = inspect.cleandoc(chat_message)
            return chat_message
        else:
            raise ValueError(f"Invalid message for Chatbot component: {chat_message}")

    def postprocess(
        self,
        y: list[list[str | tuple[str] | tuple[str, str] | None] | tuple],
    ) -> list[list[str | dict | None]]:
        """
        Parameters:
            y: List of lists representing the message and response pairs. Each message and response should be a string, which may be in Markdown format.  It can also be a tuple whose first element is a string or pathlib.Path filepath or URL to an image/video/audio, and second (optional) element is the alt text, in which case the media file is displayed. It can also be None, in which case that message is not displayed.
        Returns:
            List of lists representing the message and response. Each message and response will be a string of HTML, or a dictionary with media information. Or None if the message is not to be displayed.
        """
        if y is None:
            return []
        processed_messages = []
        for message_pair in y:
            assert isinstance(
                message_pair, (tuple, list)
            ), f"Expected a list of lists or list of tuples. Received: {message_pair}"
            assert (
                len(message_pair) == 2
            ), f"Expected a list of lists of length 2 or list of tuples of length 2. Received: {message_pair}"
            processed_messages.append(
                [
                    self._postprocess_chat_messages(message_pair[0]),
                    self._postprocess_chat_messages(message_pair[1]),
                ]
            )
        return processed_messages

    def style(self, height: int | None = None, **kwargs):
        """
        This method is deprecated. Please set these arguments in the constructor instead.
        """
        warn_style_method_deprecation()
        if height is not None:
            self.height = height
        return self
