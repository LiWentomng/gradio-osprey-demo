# Upcoming Release

## New Features:

No changes to highlight.

## Bug Fixes:

No changes to highlight.

## Other Changes:

- Warning on mobile that if a user leaves the tab, websocket connection may break. On broken connection, tries to rejoin queue and displays error conveying connection broke. By [@aliabid94](https://github.com/aliabid94) in [PR 4742](https://github.com/gradio-app/gradio/pull/4742)

## Breaking Changes:

No changes to highlight.

# Version 3.36.1

## New Features:

- Hotfix to support pydantic v1 and v2 by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4835](https://github.com/gradio-app/gradio/pull/4835)

## Bug Fixes:

No changes to highlight.

## Other Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

# Version 3.36.0

## New Features:

- The `gr.Video`, `gr.Audio`, `gr.Image`, `gr.Chatbot`, and `gr.Gallery` components now include a share icon when deployed on Spaces. This behavior can be modified by setting the `show_share_button` parameter in the component classes. by [@aliabid94](https://github.com/aliabid94) in [PR 4651](https://github.com/gradio-app/gradio/pull/4651)
- Allow the web component `space`, `src`, and `host` attributes to be updated dynamically by [@pngwn](https://github.com/pngwn) in [PR 4461](https://github.com/gradio-app/gradio/pull/4461)
- Suggestion for Spaces Duplication built into Gradio, by [@aliabid94](https://github.com/aliabid94) in [PR 4458](https://github.com/gradio-app/gradio/pull/4458)
- The `api_name` parameter now accepts `False` as a value, which means it does not show up in named or unnamed endpoints. By [@abidlabs](https://github.com/aliabid94) in [PR 4683](https://github.com/gradio-app/gradio/pull/4683)
- Added support for `pathlib.Path` in `gr.Video`, `gr.Gallery`, and `gr.Chatbot` by [sunilkumardash9](https://github.com/sunilkumardash9) in [PR 4581](https://github.com/gradio-app/gradio/pull/4581).

## Bug Fixes:

- Updated components with `info` attribute to update when `update()` is called on them.  by [@jebarpg](https://github.com/jebarpg) in [PR 4715](https://github.com/gradio-app/gradio/pull/4715).
- Ensure the `Image` components undo button works mode is `mask` or `color-sketch` by [@amyorz](https://github.com/AmyOrz) in [PR 4692](https://github.com/gradio-app/gradio/pull/4692)
- Load the iframe resizer external asset asynchronously, by [@akx](https://github.com/akx) in [PR 4336](https://github.com/gradio-app/gradio/pull/4336)
- Restored missing imports in `gr.components` by [@abidlabs](https://github.com/abidlabs) in [PR 4566](https://github.com/gradio-app/gradio/pull/4566)
- Fix bug where `select` event was not triggered in `gr.Gallery` if `height` was set to be large with `allow_preview=False` by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4551](https://github.com/gradio-app/gradio/pull/4551)
- Fix bug where setting `visible=False` in `gr.Group` event did not work by [@abidlabs](https://github.com/abidlabs) in [PR 4567](https://github.com/gradio-app/gradio/pull/4567)
- Fix `make_waveform` to work with paths that contain spaces [@akx](https://github.com/akx) in [PR 4570](https://github.com/gradio-app/gradio/pull/4570) & [PR 4578](https://github.com/gradio-app/gradio/pull/4578)
- Send captured data in `stop_recording` event for `gr.Audio` and `gr.Video` components by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4554](https://github.com/gradio-app/gradio/pull/4554)
- Fix bug in `gr.Gallery` where `height` and `object_fit` parameters where being ignored by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4576](https://github.com/gradio-app/gradio/pull/4576)
- Fixes an HTML sanitization issue in DOMPurify where links in markdown were not opening in a new window by [@hannahblair] in [PR 4577](https://github.com/gradio-app/gradio/pull/4577)
- Fixed Dropdown height rendering in Columns by [@aliabid94](https://github.com/aliabid94) in [PR 4584](https://github.com/gradio-app/gradio/pull/4584) 
- Fixed bug where `AnnotatedImage` css styling was causing the annotation masks to not be displayed correctly by  [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4628](https://github.com/gradio-app/gradio/pull/4628)
- Ensure that Gradio does not silently fail when running on a port that is occupied by [@abidlabs](https://github.com/abidlabs) in [PR 4624](https://github.com/gradio-app/gradio/pull/4624).
- Fix double upload bug that caused lag in file uploads by [@aliabid94](https://github.com/aliabid94) in [PR 4661](https://github.com/gradio-app/gradio/pull/4661)
- `Progress` component now appears even when no `iterable` is specified in `tqdm` constructor by [@itrushkin](https://github.com/itrushkin) in [PR 4475](https://github.com/gradio-app/gradio/pull/4475)
- Deprecation warnings now point at the user code using those deprecated features, instead of Gradio internals, by (https://github.com/akx) in [PR 4694](https://github.com/gradio-app/gradio/pull/4694)
- Adapt column widths in gr.Examples based on content  by [@pngwn](https://github.com/pngwn) & [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4700](https://github.com/gradio-app/gradio/pull/4700)
- The `plot` parameter deprecation warnings should now only be emitted for `Image` components by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4709](https://github.com/gradio-app/gradio/pull/4709)
- Removed uncessessary `type` deprecation warning by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4709](https://github.com/gradio-app/gradio/pull/4709)
- Ensure Audio autoplays works when `autoplay=True` and the video source is dynamically updated [@pngwn](https://github.com/pngwn) in [PR 4705](https://github.com/gradio-app/gradio/pull/4705)
- When an error modal is shown in spaces, ensure we scroll to the top so it can be seen by [@pngwn](https://github.com/pngwn) in [PR 4712](https://github.com/gradio-app/gradio/pull/4712)
- Update depedencies by [@pngwn](https://github.com/pngwn) in [PR 4675](https://github.com/gradio-app/gradio/pull/4675)
- Fixes `gr.Dropdown` being cutoff at the bottom by [@abidlabs](https://github.com/abidlabs) in [PR 4691](https://github.com/gradio-app/gradio/pull/4691).
- Scroll top when clicking "View API" in spaces by [@pngwn](https://github.com/pngwn) in [PR 4714](https://github.com/gradio-app/gradio/pull/4714)
- Fix bug where `show_label` was hiding the entire component for `gr.Label` by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4713](https://github.com/gradio-app/gradio/pull/4713)
- Don't crash when uploaded image has broken EXIF data, by [@akx](https://github.com/akx) in [PR 4764](https://github.com/gradio-app/gradio/pull/4764)
- Place toast messages at the top of the screen by [@pngwn](https://github.com/pngwn) in [PR 4796](https://github.com/gradio-app/gradio/pull/4796)
- Fix regressed styling of Login page when auth is enabled by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4797](https://github.com/gradio-app/gradio/pull/4797)
- Prevent broken scrolling to output on Spaces by [@aliabid94](https://github.com/aliabid94) in [PR 4822](https://github.com/gradio-app/gradio/pull/4822)

## Other Changes:

- Add `.git-blame-ignore-revs` by [@akx](https://github.com/akx) in [PR 4586](https://github.com/gradio-app/gradio/pull/4586)
- Update frontend dependencies in [PR 4601](https://github.com/gradio-app/gradio/pull/4601)
- Use `typing.Literal` where possible in gradio library and client by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4608](https://github.com/gradio-app/gradio/pull/4608)
- Remove unnecessary mock json files for frontend E2E tests by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4625](https://github.com/gradio-app/gradio/pull/4625)
- Update dependencies by [@pngwn](https://github.com/pngwn) in [PR 4643](https://github.com/gradio-app/gradio/pull/4643)
- The theme builder now launches successfully, and the API docs are cleaned up. By [@abidlabs](https://github.com/aliabid94) in [PR 4683](https://github.com/gradio-app/gradio/pull/4683)
- Remove `cleared_value` from some components as its no longer used internally by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4685](https://github.com/gradio-app/gradio/pull/4685)
- Better errors when you define two Blocks and reference components in one Blocks from the events in the other Blocks [@abidlabs](https://github.com/abidlabs) in [PR 4738](https://github.com/gradio-app/gradio/pull/4738).
- Better message when share link is not created by [@abidlabs](https://github.com/abidlabs) in [PR 4773](https://github.com/gradio-app/gradio/pull/4773).
- Improve accessibility around selected images in gr.Gallery component by [@hannahblair](https://github.com/hannahblair) in [PR 4790](https://github.com/gradio-app/gradio/pull/4790)

## Breaking Changes:

[PR 4683](https://github.com/gradio-app/gradio/pull/4683) removes the explict named endpoint "load_examples" from gr.Interface that was introduced in [PR 4456](https://github.com/gradio-app/gradio/pull/4456).

# Version 3.35.2

## New Features:

No changes to highlight.

## Bug Fixes:

- Fix chatbot streaming by [@aliabid94](https://github.com/aliabid94) in [PR 4537](https://github.com/gradio-app/gradio/pull/4537)
- Fix chatbot height and scrolling by [@aliabid94](https://github.com/aliabid94) in [PR 4540](https://github.com/gradio-app/gradio/pull/4540)

## Other Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

# Version 3.35.1

## New Features:

No changes to highlight.

## Bug Fixes:

- Fix chatbot streaming by [@aliabid94](https://github.com/aliabid94) in [PR 4537](https://github.com/gradio-app/gradio/pull/4537)
- Fix error modal position and text size by [@pngwn](https://github.com/pngwn) in [PR 4538](https://github.com/gradio-app/gradio/pull/4538).

## Other Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

# Version 3.35.0

## New Features:

- A `gr.ClearButton` which allows users to easily clear the values of components by [@abidlabs](https://github.com/abidlabs) in [PR 4456](https://github.com/gradio-app/gradio/pull/4456)

Example usage:

```py
import gradio as gr

with gr.Blocks() as demo:
    chatbot = gr.Chatbot([("Hello", "How are you?")])
    with gr.Row():
        textbox = gr.Textbox(scale=3, interactive=True)
        gr.ClearButton([textbox, chatbot], scale=1)

demo.launch()
```

- Min and max value for gr.Number by [@artegoser](https://github.com/artegoser) and [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3991](https://github.com/gradio-app/gradio/pull/3991)
- Add `start_recording` and `stop_recording` events to `Video` and `Audio` components by [@pngwn](https://github.com/pngwn) in [PR 4422](https://github.com/gradio-app/gradio/pull/4422)
- Allow any function to generate an error message and allow multiple messages to appear at a time. Other error modal improvements such as auto dismiss after a time limit and a new layout on mobile [@pngwn](https://github.com/pngwn) in [PR 4459](https://github.com/gradio-app/gradio/pull/4459).
- Add `autoplay` kwarg to `Video` and `Audio` components by [@pngwn](https://github.com/pngwn) in [PR 4453](https://github.com/gradio-app/gradio/pull/4453)
- Add `allow_preview` parameter to `Gallery` to control whether a detailed preview is displayed on click by
[@freddyaboulton](https://github.com/freddyaboulton) in [PR 4470](https://github.com/gradio-app/gradio/pull/4470)
- Add `latex_delimiters` parameter to `Chatbot` to control the delimiters used for LaTeX and to disable LaTeX in the `Chatbot` by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4516](https://github.com/gradio-app/gradio/pull/4516)
- Can now issue `gr.Warning` and `gr.Info` modals. Simply put the code `gr.Warning("Your warning message")` or `gr.Info("Your info message")` as a standalone line in your function. By [@aliabid94](https://github.com/aliabid94) in [PR 4518](https://github.com/gradio-app/gradio/pull/4518). 

Example:
```python
def start_process(name):
    gr.Info("Starting process")
    if name is None:
        gr.Warning("Name is empty")
    ...
    if success == False:
        raise gr.Error("Process failed")
```


## Bug Fixes:

- Add support for PAUSED state in the JS client by [@abidlabs](https://github.com/abidlabs) in [PR 4438](https://github.com/gradio-app/gradio/pull/4438)
- Ensure Tabs only occupy the space required by [@pngwn](https://github.com/pngwn) in [PR 4419](https://github.com/gradio-app/gradio/pull/4419)
- Ensure components have the correct empty sizes to prevent empty containers from collapsing by [@pngwn](https://github.com/pngwn) in [PR 4447](https://github.com/gradio-app/gradio/pull/4447).
- Frontend code no longer crashes when there is a relative URL in an `<a>` element, by [@akx](https://github.com/akx) in [PR 4449](https://github.com/gradio-app/gradio/pull/4449).
- Fix bug where setting `format='mp4'` on a video component would cause the function to error out if the uploaded video was not playable by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4467](https://github.com/gradio-app/gradio/pull/4467)
- Fix `_js` parameter to work even without backend function, by [@aliabid94](https://github.com/aliabid94) in [PR 4486](https://github.com/gradio-app/gradio/pull/4486).
- Fix new line issue with `gr.Chatbot()` by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4491](https://github.com/gradio-app/gradio/pull/4491)
- Fixes issue with Clear button not working for `Label` component by [@abidlabs](https://github.com/abidlabs) in [PR 4456](https://github.com/gradio-app/gradio/pull/4456)
- Restores the ability to pass in a tuple (sample rate, audio array) to gr.Audio() by [@abidlabs](https://github.com/abidlabs) in [PR 4525](https://github.com/gradio-app/gradio/pull/4525)
- Ensure code is correctly formatted and copy button is always present in Chatbot by [@pngwn](https://github.com/pngwn) in [PR 4527](https://github.com/gradio-app/gradio/pull/4527)
- `show_label` will not automatically be set to `True` in `gr.BarPlot.update` by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4531](https://github.com/gradio-app/gradio/pull/4531)
- `gr.BarPlot` group text now respects darkmode by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4531](https://github.com/gradio-app/gradio/pull/4531)
- Fix dispatched errors from within components [@aliabid94](https://github.com/aliabid94) in [PR 4786](https://github.com/gradio-app/gradio/pull/4786)

## Other Changes:

- Change styling of status and toast error components by [@hannahblair](https://github.com/hannahblair) in [PR 4454](https://github.com/gradio-app/gradio/pull/4454).
- Clean up unnecessary `new Promise()`s by [@akx](https://github.com/akx) in [PR 4442](https://github.com/gradio-app/gradio/pull/4442).
- Minor UI cleanup for Examples and Dataframe components [@aliabid94](https://github.com/aliabid94) in [PR 4455](https://github.com/gradio-app/gradio/pull/4455). 
- Minor UI cleanup for Examples and Dataframe components [@aliabid94](https://github.com/aliabid94) in [PR 4455](https://github.com/gradio-app/gradio/pull/4455).
- Add Catalan translation [@jordimas](https://github.com/jordimas) in [PR 4483](https://github.com/gradio-app/gradio/pull/4483).
- The API endpoint that loads examples upon click has been given an explicit name ("/load_examples") by [@abidlabs](https://github.com/abidlabs) in [PR 4456](https://github.com/gradio-app/gradio/pull/4456).
- Allows configuration of FastAPI app when calling `mount_gradio_app`, by [@charlesfrye](https://github.com/charlesfrye) in [PR4519](https://github.com/gradio-app/gradio/pull/4519).

## Breaking Changes:

- The behavior of the `Clear` button has been changed for `Slider`, `CheckboxGroup`, `Radio`, `Dropdown` components by [@abidlabs](https://github.com/abidlabs) in [PR 4456](https://github.com/gradio-app/gradio/pull/4456). The Clear button now sets the value of these components to be empty as opposed to the original default set by the developer. This is to make them in line with the rest of the Gradio components.
- Python 3.7 end of life is June 27 2023. Gradio will no longer support python 3.7 by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4484](https://github.com/gradio-app/gradio/pull/4484)
- Removed `$` as a default LaTeX delimiter for the `Chatbot` by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4516](https://github.com/gradio-app/gradio/pull/4516). The specific LaTeX delimeters can be set using the new `latex_delimiters` parameter in `Chatbot`.

# Version 3.34.0

## New Features:

- The `gr.UploadButton` component now supports the `variant` and `interactive` parameters by [@abidlabs](https://github.com/abidlabs) in [PR 4436](https://github.com/gradio-app/gradio/pull/4436).

## Bug Fixes:

- Remove target="\_blank" override on anchor tags with internal targets by [@hannahblair](https://github.com/hannahblair) in [PR 4405](https://github.com/gradio-app/gradio/pull/4405)
- Fixed bug where `gr.File(file_count='multiple')` could not be cached as output by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4421](https://github.com/gradio-app/gradio/pull/4421)
- Restricts the domains that can be proxied via `/proxy` route by [@abidlabs](https://github.com/abidlabs) in [PR 4406](https://github.com/gradio-app/gradio/pull/4406).
- Fixes issue where `gr.UploadButton` could not be used to upload the same file twice by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4437](https://github.com/gradio-app/gradio/pull/4437)
- Fixes bug where `/proxy` route was being incorrectly constructed by the frontend by [@abidlabs](https://github.com/abidlabs) in [PR 4430](https://github.com/gradio-app/gradio/pull/4430).
- Fix z-index of status component by [@hannahblair](https://github.com/hannahblair) in [PR 4429](https://github.com/gradio-app/gradio/pull/4429)
- Fix video rendering in Safari by [@aliabid94](https://github.com/aliabid94) in [PR 4433](https://github.com/gradio-app/gradio/pull/4433).
- The output directory for files downloaded when calling Blocks as a function is now set to a temporary directory by default (instead of the working directory in some cases) by [@abidlabs](https://github.com/abidlabs) in [PR 4501](https://github.com/gradio-app/gradio/pull/4501)

## Other Changes:

- When running on Spaces, handler functions will be transformed by the [PySpaces](https://pypi.org/project/spaces/) library in order to make them work with specific hardware. It will have no effect on standalone Gradio apps or regular Gradio Spaces and can be globally deactivated as follows : `import spaces; spaces.disable_gradio_auto_wrap()` by [@cbensimon](https://github.com/cbensimon) in [PR 4389](https://github.com/gradio-app/gradio/pull/4389).
- Deprecated `.style` parameter and moved arguments to constructor. Added support for `.update()` to all arguments initially in style. Added `scale` and `min_width` support to every Component. By [@aliabid94](https://github.com/aliabid94) in [PR 4374](https://github.com/gradio-app/gradio/pull/4374)

## Breaking Changes:

No changes to highlight.

# Version 3.33.1

## New Features:

No changes to highlight.

## Bug Fixes:

- Allow `every` to work with generators by [@dkjshk](https://github.com/dkjshk) in [PR 4434](https://github.com/gradio-app/gradio/pull/4434)
- Fix z-index of status component by [@hannahblair](https://github.com/hannahblair) in [PR 4429](https://github.com/gradio-app/gradio/pull/4429)
- Allow gradio to work offline, by [@aliabid94](https://github.com/aliabid94) in [PR 4398](https://github.com/gradio-app/gradio/pull/4398).
- Fixed `validate_url` to check for 403 errors and use a GET request in place of a HEAD by [@alvindaiyan](https://github.com/alvindaiyan) in [PR 4388](https://github.com/gradio-app/gradio/pull/4388).

## Other Changes:

- More explicit error message when share link binary is blocked by antivirus by [@abidlabs](https://github.com/abidlabs) in [PR 4380](https://github.com/gradio-app/gradio/pull/4380).

## Breaking Changes:

No changes to highlight.

# Version 3.33.0

## New Features:

- Introduced `gradio deploy` to launch a Gradio app to Spaces directly from your terminal. By [@aliabid94](https://github.com/aliabid94) in [PR 4033](https://github.com/gradio-app/gradio/pull/4033).
- Introduce `show_progress='corner'` argument to event listeners, which will not cover the output components with the progress animation, but instead show it in the corner of the components. By [@aliabid94](https://github.com/aliabid94) in [PR 4396](https://github.com/gradio-app/gradio/pull/4396).

## Bug Fixes:

- Fix bug where Label change event was triggering itself by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4371](https://github.com/gradio-app/gradio/pull/4371)
- Make `Blocks.load` behave like other event listeners (allows chaining `then` off of it) [@anentropic](https://github.com/anentropic/) in [PR 4304](https://github.com/gradio-app/gradio/pull/4304)
- Respect `interactive=True` in output components of a `gr.Interface` by [@abidlabs](https://github.com/abidlabs) in [PR 4356](https://github.com/gradio-app/gradio/pull/4356).
- Remove unused frontend code by [@akx](https://github.com/akx) in [PR 4275](https://github.com/gradio-app/gradio/pull/4275)
- Fixes favicon path on Windows by [@abidlabs](https://github.com/abidlabs) in [PR 4369](https://github.com/gradio-app/gradio/pull/4369).
- Prevent path traversal in `/file` routes by [@abidlabs](https://github.com/abidlabs) in [PR 4370](https://github.com/gradio-app/gradio/pull/4370).
- Do not send HF token to other domains via `/proxy` route by [@abidlabs](https://github.com/abidlabs) in [PR 4368](https://github.com/gradio-app/gradio/pull/4368).
- Replace default `markedjs` sanitize function with DOMPurify sanitizer for `gr.Chatbot()` by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4360](https://github.com/gradio-app/gradio/pull/4360)
- Prevent the creation of duplicate copy buttons in the chatbot and ensure copy buttons work in non-secure contexts by [@binary-husky](https://github.com/binary-husky) in [PR 4350](https://github.com/gradio-app/gradio/pull/4350).

## Other Changes:

- Remove flicker of loading bar by adding opacity transition, by [@aliabid94](https://github.com/aliabid94) in [PR 4349](https://github.com/gradio-app/gradio/pull/4349).
- Performance optimization in the frontend's Blocks code by [@akx](https://github.com/akx) in [PR 4334](https://github.com/gradio-app/gradio/pull/4334)
- Upgrade the pnpm lock file format version from v6.0 to v6.1 by [@whitphx](https://github.com/whitphx) in [PR 4393](https://github.com/gradio-app/gradio/pull/4393)

## Breaking Changes:

- The `/file=` route no longer allows accessing dotfiles or files in "dot directories" by [@akx](https://github.com/akx) in [PR 4303](https://github.com/gradio-app/gradio/pull/4303)

# Version 3.32.0

## New Features:

- `Interface.launch()` and `Blocks.launch()` now accept an `app_kwargs` argument to allow customizing the configuration of the underlying FastAPI app, by [@akx](https://github.com/akx) in [PR 4282](https://github.com/gradio-app/gradio/pull/4282)

## Bug Fixes:

- Fixed Gallery/AnnotatedImage components not respecting GRADIO_DEFAULT_DIR variable by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4256](https://github.com/gradio-app/gradio/pull/4256)
- Fixed Gallery/AnnotatedImage components resaving identical images by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4256](https://github.com/gradio-app/gradio/pull/4256)
- Fixed Audio/Video/File components creating empty tempfiles on each run by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4256](https://github.com/gradio-app/gradio/pull/4256)
- Fixed the behavior of the `run_on_click` parameter in `gr.Examples` by [@abidlabs](https://github.com/abidlabs) in [PR 4258](https://github.com/gradio-app/gradio/pull/4258).
- Ensure error modal displays when the queue is enabled by [@pngwn](https://github.com/pngwn) in [PR 4273](https://github.com/gradio-app/gradio/pull/4273)
- Ensure js client respcts the full root when making requests to the server by [@pngwn](https://github.com/pngwn) in [PR 4271](https://github.com/gradio-app/gradio/pull/4271)

## Other Changes:

- Refactor web component `initial_height` attribute by [@whitphx](https://github.com/whitphx) in [PR 4223](https://github.com/gradio-app/gradio/pull/4223)
- Relocate `mount_css` fn to remove circular dependency [@whitphx](https://github.com/whitphx) in [PR 4222](https://github.com/gradio-app/gradio/pull/4222)
- Upgrade Black to 23.3 by [@akx](https://github.com/akx) in [PR 4259](https://github.com/gradio-app/gradio/pull/4259)
- Add frontend LaTeX support in `gr.Chatbot()` using `KaTeX` by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4285](https://github.com/gradio-app/gradio/pull/4285).

## Breaking Changes:

No changes to highlight.

# Version 3.31.0

## New Features:

- The reloader command (`gradio app.py`) can now accept command line arguments by [@micky2be](https://github.com/micky2be) in [PR 4119](https://github.com/gradio-app/gradio/pull/4119)
- Added `format` argument to `Audio` component by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4178](https://github.com/gradio-app/gradio/pull/4178)
- Add JS client code snippets to use via api page by [@aliabd](https://github.com/aliabd) in [PR 3927](https://github.com/gradio-app/gradio/pull/3927).
- Update to the JS client by [@pngwn](https://github.com/pngwn) in [PR 4202](https://github.com/gradio-app/gradio/pull/4202)

## Bug Fixes:

- Fix "TypeError: issubclass() arg 1 must be a class" When use Optional[Types] by [@lingfengchencn](https://github.com/lingfengchencn) in [PR 4200](https://github.com/gradio-app/gradio/pull/4200).
- Gradio will no longer send any analytics or call home if analytics are disabled with the GRADIO_ANALYTICS_ENABLED environment variable. By [@akx](https://github.com/akx) in [PR 4194](https://github.com/gradio-app/gradio/pull/4194) and [PR 4236](https://github.com/gradio-app/gradio/pull/4236)
- The deprecation warnings for kwargs now show the actual stack level for the invocation, by [@akx](https://github.com/akx) in [PR 4203](https://github.com/gradio-app/gradio/pull/4203).
- Fix "TypeError: issubclass() arg 1 must be a class" When use Optional[Types] by [@lingfengchencn](https://github.com/lingfengchencn) in [PR 4200](https://github.com/gradio-app/gradio/pull/4200).
- Ensure cancelling functions work correctly by [@pngwn](https://github.com/pngwn) in [PR 4225](https://github.com/gradio-app/gradio/pull/4225)
- Fixes a bug with typing.get_type_hints() on Python 3.9 by [@abidlabs](https://github.com/abidlabs) in [PR 4228](https://github.com/gradio-app/gradio/pull/4228).
- Fixes JSONDecodeError by [@davidai](https://github.com/davidai) in [PR 4241](https://github.com/gradio-app/gradio/pull/4241)
- Fix `chatbot_dialogpt` demo by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4238](https://github.com/gradio-app/gradio/pull/4238).

## Other Changes:

- Change `gr.Chatbot()` markdown parsing to frontend using `marked` library and `prism` by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4150](https://github.com/gradio-app/gradio/pull/4150)
- Update the js client by [@pngwn](https://github.com/pngwn) in [PR 3899](https://github.com/gradio-app/gradio/pull/3899)
- Fix documentation for the shape of the numpy array produced by the `Image` component by [@der3318](https://github.com/der3318) in [PR 4204](https://github.com/gradio-app/gradio/pull/4204).
- Updates the timeout for websocket messaging from 1 second to 5 seconds by [@abidlabs](https://github.com/abidlabs) in [PR 4235](https://github.com/gradio-app/gradio/pull/4235)

## Breaking Changes:

No changes to highlight.

# Version 3.30.0

## New Features:

- Adds a `root_path` parameter to `launch()` that allows running Gradio applications on subpaths (e.g. www.example.com/app) behind a proxy, by [@abidlabs](https://github.com/abidlabs) in [PR 4133](https://github.com/gradio-app/gradio/pull/4133)
- Fix dropdown change listener to trigger on change when updated as an output by [@aliabid94](https://github.com/aliabid94) in [PR 4128](https://github.com/gradio-app/gradio/pull/4128).
- Add `.input` event listener, which is only triggered when a user changes the component value (as compared to `.change`, which is also triggered when a component updates as the result of a function trigger), by [@aliabid94](https://github.com/aliabid94) in [PR 4157](https://github.com/gradio-app/gradio/pull/4157).

## Bug Fixes:

- Records username when flagging by [@abidlabs](https://github.com/abidlabs) in [PR 4135](https://github.com/gradio-app/gradio/pull/4135)
- Fix website build issue by [@aliabd](https://github.com/aliabd) in [PR 4142](https://github.com/gradio-app/gradio/pull/4142)
- Fix lang agnostic type info for `gr.File(file_count='multiple')` output components by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4153](https://github.com/gradio-app/gradio/pull/4153)

## Other Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

# Version 3.29.0

## New Features:

- Returning language agnostic types in the `/info` route by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4039](https://github.com/gradio-app/gradio/pull/4039)

## Bug Fixes:

- Allow users to upload audio files in Audio component on iOS by by [@aliabid94](https://github.com/aliabid94) in [PR 4071](https://github.com/gradio-app/gradio/pull/4071).
- Fixes the gradio theme builder error that appeared on launch by [@aliabid94](https://github.com/aliabid94) and [@abidlabs](https://github.com/abidlabs) in [PR 4080](https://github.com/gradio-app/gradio/pull/4080)
- Keep Accordion content in DOM by [@aliabid94](https://github.com/aliabid94) in [PR 4070](https://github.com/gradio-app/gradio/pull/4073)
- Fixed bug where type hints in functions caused the event handler to crash by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 4068](https://github.com/gradio-app/gradio/pull/4068)
- Fix dropdown default value not appearing by [@aliabid94](https://github.com/aliabid94) in [PR 4072](https://github.com/gradio-app/gradio/pull/4072).
- Soft theme label color fix by [@aliabid94](https://github.com/aliabid94) in [PR 4070](https://github.com/gradio-app/gradio/pull/4070)
- Fix `gr.Slider` `release` event not triggering on mobile by [@space-nuko](https://github.com/space-nuko) in [PR 4098](https://github.com/gradio-app/gradio/pull/4098)
- Removes extraneous `State` component info from the `/info` route by [@abidlabs](https://github.com/freddyaboulton) in [PR 4107](https://github.com/gradio-app/gradio/pull/4107)
- Make .then() work even if first event fails by [@aliabid94](https://github.com/aliabid94) in [PR 4115](https://github.com/gradio-app/gradio/pull/4115).

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Allow users to submit with enter in Interfaces with textbox / number inputs [@aliabid94](https://github.com/aliabid94) in [PR 4090](https://github.com/gradio-app/gradio/pull/4090).
- Updates gradio's requirements.txt to requires uvicorn>=0.14.0 by [@abidlabs](https://github.com/abidlabs) in [PR 4086](https://github.com/gradio-app/gradio/pull/4086)
- Updates some error messaging by [@abidlabs](https://github.com/abidlabs) in [PR 4086](https://github.com/gradio-app/gradio/pull/4086)
- Renames simplified Chinese translation file from `zh-cn.json` to `zh-CN.json` by [@abidlabs](https://github.com/abidlabs) in [PR 4086](https://github.com/gradio-app/gradio/pull/4086)

## Contributors Shoutout:

No changes to highlight.

# Version 3.28.3

## New Features:

No changes to highlight.

## Bug Fixes:

- Fixes issue with indentation in `gr.Code()` component with streaming by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4043](https://github.com/gradio-app/gradio/pull/4043)

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.28.2

## Bug Fixes

- Code component visual updates by [@pngwn](https://github.com/pngwn) in [PR 4051](https://github.com/gradio-app/gradio/pull/4051)

## New Features:

- Add support for `visual-question-answering`, `document-question-answering`, and `image-to-text` using `gr.Interface.load("models/...")` and `gr.Interface.from_pipeline` by [@osanseviero](https://github.com/osanseviero) in [PR 3887](https://github.com/gradio-app/gradio/pull/3887)
- Add code block support in `gr.Chatbot()`, by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 4048](https://github.com/gradio-app/gradio/pull/4048)
- Adds the ability to blocklist filepaths (and also improves the allowlist mechanism) by [@abidlabs](https://github.com/abidlabs) in [PR 4047](https://github.com/gradio-app/gradio/pull/4047).
- Adds the ability to specify the upload directory via an environment variable by [@abidlabs](https://github.com/abidlabs) in [PR 4047](https://github.com/gradio-app/gradio/pull/4047).

## Bug Fixes:

- Fixes issue with `matplotlib` not rendering correctly if the backend was not set to `Agg` by [@abidlabs](https://github.com/abidlabs) in [PR 4029](https://github.com/gradio-app/gradio/pull/4029)
- Fixes bug where rendering the same `gr.State` across different Interfaces/Blocks within larger Blocks would not work by [@abidlabs](https://github.com/abidlabs) in [PR 4030](https://github.com/gradio-app/gradio/pull/4030)
- Code component visual updates by [@pngwn](https://github.com/pngwn) in [PR 4051](https://github.com/gradio-app/gradio/pull/4051)

## Documentation Changes:

- Adds a Guide on how to use the Python Client within a FastAPI app, by [@abidlabs](https://github.com/abidlabs) in [PR 3892](https://github.com/gradio-app/gradio/pull/3892)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

- `gr.HuggingFaceDatasetSaver` behavior changed internally. The `flagging/` folder is not a `.git/` folder anymore when using it. `organization` parameter is now ignored in favor of passing a full dataset id as `dataset_name` (e.g. `"username/my-dataset"`).
- New lines (`\n`) are not automatically converted to `<br>` in `gr.Markdown()` or `gr.Chatbot()`. For multiple new lines, a developer must add multiple `<br>` tags.

## Full Changelog:

- Safer version of `gr.HuggingFaceDatasetSaver` using HTTP methods instead of git pull/push by [@Wauplin](https://github.com/Wauplin) in [PR 3973](https://github.com/gradio-app/gradio/pull/3973)

## Contributors Shoutout:

No changes to highlight.

# Version 3.28.1

## New Features:

- Add a "clear mask" button to `gr.Image` sketch modes, by [@space-nuko](https://github.com/space-nuko) in [PR 3615](https://github.com/gradio-app/gradio/pull/3615)

## Bug Fixes:

- Fix dropdown default value not appearing by [@aliabid94](https://github.com/aliabid94) in [PR 3996](https://github.com/gradio-app/gradio/pull/3996).
- Fix faded coloring of output textboxes in iOS / Safari by [@aliabid94](https://github.com/aliabid94) in [PR 3993](https://github.com/gradio-app/gradio/pull/3993)

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

- CI: Simplified Python CI workflow by [@akx](https://github.com/akx) in [PR 3982](https://github.com/gradio-app/gradio/pull/3982)
- Upgrade pyright to 1.1.305 by [@akx](https://github.com/akx) in [PR 4042](https://github.com/gradio-app/gradio/pull/4042)
- More Ruff rules are enabled and lint errors fixed by [@akx](https://github.com/akx) in [PR 4038](https://github.com/gradio-app/gradio/pull/4038)

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.28.0

## Bug Fixes:

- Fix duplicate play commands in full-screen mode of 'video'. by [@tomchang25](https://github.com/tomchang25) in [PR 3968](https://github.com/gradio-app/gradio/pull/3968).
- Fix the issue of the UI stuck caused by the 'selected' of DataFrame not being reset. by [@tomchang25](https://github.com/tomchang25) in [PR 3916](https://github.com/gradio-app/gradio/pull/3916).
- Fix issue where `gr.Video()` would not work inside a `gr.Tab()` by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3891](https://github.com/gradio-app/gradio/pull/3891)
- Fixed issue with old_value check in File. by [@tomchang25](https://github.com/tomchang25) in [PR 3859](https://github.com/gradio-app/gradio/pull/3859).
- Fixed bug where all bokeh plots appeared in the same div by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3896](https://github.com/gradio-app/gradio/pull/3896)
- Fixed image outputs to automatically take full output image height, unless explicitly set, by [@aliabid94](https://github.com/aliabid94) in [PR 3905](https://github.com/gradio-app/gradio/pull/3905)
- Fix issue in `gr.Gallery()` where setting height causes aspect ratio of images to collapse by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3830](https://github.com/gradio-app/gradio/pull/3830)
- Fix issue where requesting for a non-existing file would trigger a 500 error by [@micky2be](https://github.com/micky2be) in `[PR 3895](https://github.com/gradio-app/gradio/pull/3895)`.
- Fix bugs with abspath about symlinks, and unresolvable path on Windows by [@micky2be](https://github.com/micky2be) in `[PR 3895](https://github.com/gradio-app/gradio/pull/3895)`.
- Fixes type in client `Status` enum by [@10zinten](https://github.com/10zinten) in [PR 3931](https://github.com/gradio-app/gradio/pull/3931)
- Fix `gr.ChatBot` to handle image url [tye-singwa](https://github.com/tye-signwa) in [PR 3953](https://github.com/gradio-app/gradio/pull/3953)
- Move Google Tag Manager related initialization code to analytics-enabled block by [@akx](https://github.com/akx) in [PR 3956](https://github.com/gradio-app/gradio/pull/3956)
- Fix bug where port was not reused if the demo was closed and then re-launched by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3896](https://github.com/gradio-app/gradio/pull/3959)
- Fixes issue where dropdown does not position itself at selected element when opened [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3639](https://github.com/gradio-app/gradio/pull/3639)

## Documentation Changes:

- Make use of `gr` consistent across the docs by [@duerrsimon](https://github.com/duerrsimon) in [PR 3901](https://github.com/gradio-app/gradio/pull/3901)
- Fixed typo in theming-guide.md by [@eltociear](https://github.com/eltociear) in [PR 3952](https://github.com/gradio-app/gradio/pull/3952)

## Testing and Infrastructure Changes:

- CI: Python backend lint is only run once, by [@akx](https://github.com/akx) in [PR 3960](https://github.com/gradio-app/gradio/pull/3960)
- Format invocations and concatenations were replaced by f-strings where possible by [@akx](https://github.com/akx) in [PR 3984](https://github.com/gradio-app/gradio/pull/3984)
- Linting rules were made more strict and issues fixed by [@akx](https://github.com/akx) in [PR 3979](https://github.com/gradio-app/gradio/pull/3979).

## Breaking Changes:

- Some re-exports in `gradio.themes` utilities (introduced in 3.24.0) have been eradicated.
  By [@akx](https://github.com/akx) in [PR 3958](https://github.com/gradio-app/gradio/pull/3958)

## Full Changelog:

- Add DESCRIPTION.md to image_segmentation demo by [@aliabd](https://github.com/aliabd) in [PR 3866](https://github.com/gradio-app/gradio/pull/3866)
- Fix error in running `gr.themes.builder()` by [@deepkyu](https://github.com/deepkyu) in [PR 3869](https://github.com/gradio-app/gradio/pull/3869)
- Fixed a JavaScript TypeError when loading custom JS with `_js` and setting `outputs` to `None` in `gradio.Blocks()` by [@DavG25](https://github.com/DavG25) in [PR 3883](https://github.com/gradio-app/gradio/pull/3883)
- Fixed bg_background_fill theme property to expand to whole background, block_radius to affect form elements as well, and added block_label_shadow theme property by [@aliabid94](https://github.com/aliabid94) in [PR 3590](https://github.com/gradio-app/gradio/pull/3590)

## Contributors Shoutout:

No changes to highlight.

# Version 3.27.0

## New Features:

### AnnotatedImage Component

New AnnotatedImage component allows users to highlight regions of an image, either by providing bounding boxes, or 0-1 pixel masks. This component is useful for tasks such as image segmentation, object detection, and image captioning.

![AnnotatedImage screenshot](https://user-images.githubusercontent.com/7870876/232142720-86e0020f-beaf-47b9-a843-689c9621f09c.gif)

Example usage:

```python
with gr.Blocks() as demo:
    img = gr.Image()
    img_section = gr.AnnotatedImage()
    def mask(img):
        top_left_corner = [0, 0, 20, 20]
        random_mask = np.random.randint(0, 2, img.shape[:2])
        return (img, [(top_left_corner, "left corner"), (random_mask, "random")])
    img.change(mask, img, img_section)
```

See the [image_segmentation demo](https://github.com/gradio-app/gradio/tree/main/demo/image_segmentation) for a full example. By [@aliabid94](https://github.com/aliabid94) in [PR 3836](https://github.com/gradio-app/gradio/pull/3836)

## Bug Fixes:

No changes to highlight.

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.26.0

## New Features:

### `Video` component supports subtitles

- Allow the video component to accept subtitles as input, by [@tomchang25](https://github.com/tomchang25) in [PR 3673](https://github.com/gradio-app/gradio/pull/3673). To provide subtitles, simply return a tuple consisting of `(path_to_video, path_to_subtitles)` from your function. Both `.srt` and `.vtt` formats are supported:

```py
with gr.Blocks() as demo:
    gr.Video(("video.mp4", "captions.srt"))
```

## Bug Fixes:

- Fix code markdown support in `gr.Chatbot()` component by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3816](https://github.com/gradio-app/gradio/pull/3816)

## Documentation Changes:

- Updates the "view API" page in Gradio apps to use the `gradio_client` library by [@aliabd](https://github.com/aliabd) in [PR 3765](https://github.com/gradio-app/gradio/pull/3765)

- Read more about how to use the `gradio_client` library here: https://gradio.app/getting-started-with-the-python-client/

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.25.0

## New Features:

- Improve error messages when number of inputs/outputs to event handlers mismatch, by [@space-nuko](https://github.com/space-nuko) in [PR 3519](https://github.com/gradio-app/gradio/pull/3519)

- Add `select` listener to Images, allowing users to click on any part of an image and get the coordinates of the click by [@aliabid94](https://github.com/aliabid94) in [PR 3786](https://github.com/gradio-app/gradio/pull/3786).

```python
with gr.Blocks() as demo:
    img = gr.Image()
    textbox = gr.Textbox()

    def select_handler(img, evt: gr.SelectData):
        selected_pixel = img[evt.index[1], evt.index[0]]
        return f"Selected pixel: {selected_pixel}"

    img.select(select_handler, img, textbox)
```

![Recording 2023-04-08 at 17 44 39](https://user-images.githubusercontent.com/7870876/230748572-90a2a8d5-116d-4769-bb53-5516555fbd0f.gif)

## Bug Fixes:

- Increase timeout for sending analytics data by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3647](https://github.com/gradio-app/gradio/pull/3647)
- Fix bug where http token was not accessed over websocket connections by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3735](https://github.com/gradio-app/gradio/pull/3735)
- Add ability to specify `rows`, `columns` and `object-fit` in `style()` for `gr.Gallery()` component by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3586](https://github.com/gradio-app/gradio/pull/3586)
- Fix bug where recording an audio file through the microphone resulted in a corrupted file name by [@abidlabs](https://github.com/abidlabs) in [PR 3770](https://github.com/gradio-app/gradio/pull/3770)
- Added "ssl_verify" to blocks.launch method to allow for use of self-signed certs by [@garrettsutula](https://github.com/garrettsutula) in [PR 3873](https://github.com/gradio-app/gradio/pull/3873)
- Fix bug where iterators where not being reset for processes that terminated early by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3777](https://github.com/gradio-app/gradio/pull/3777)
- Fix bug where the upload button was not properly handling the `file_count='multiple'` case by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3782](https://github.com/gradio-app/gradio/pull/3782)
- Fix bug where use Via API button was giving error by [@Devang-C](https://github.com/Devang-C) in [PR 3783](https://github.com/gradio-app/gradio/pull/3783)

## Documentation Changes:

- Fix invalid argument docstrings, by [@akx](https://github.com/akx) in [PR 3740](https://github.com/gradio-app/gradio/pull/3740)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Fixed IPv6 listening to work with bracket [::1] notation, by [@dsully](https://github.com/dsully) in [PR 3695](https://github.com/gradio-app/gradio/pull/3695)

## Contributors Shoutout:

No changes to highlight.

# Version 3.24.1

## New Features:

- No changes to highlight.

## Bug Fixes:

- Fixes Chatbot issue where new lines were being created every time a message was sent back and forth by [@aliabid94](https://github.com/aliabid94) in [PR 3717](https://github.com/gradio-app/gradio/pull/3717).
- Fixes data updating in DataFrame invoking a `select` event once the dataframe has been selected. By [@yiyuezhuo](https://github.com/yiyuezhuo) in [PR 3861](https://github.com/gradio-app/gradio/pull/3861)
- Fixes false positive warning which is due to too strict type checking by [@yiyuezhuo](https://github.com/yiyuezhuo) in [PR 3837](https://github.com/gradio-app/gradio/pull/3837).

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.24.0

## New Features:

- Trigger the release event when Slider number input is released or unfocused by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3589](https://github.com/gradio-app/gradio/pull/3589)
- Created Theme Builder, which allows users to create themes without writing any code, by [@aliabid94](https://github.com/aliabid94) in [PR 3664](https://github.com/gradio-app/gradio/pull/3664). Launch by:

  ```python
  import gradio as gr
  gr.themes.builder()
  ```

  ![Theme Builder](https://user-images.githubusercontent.com/7870876/228204929-d71cbba5-69c2-45b3-bd20-e3a201d98b12.png)

- The `Dropdown` component now has a `allow_custom_value` parameter that lets users type in custom values not in the original list of choices.
- The `Colorpicker` component now has a `.blur()` event

### Added a download button for videos! 📥

![download_video](https://user-images.githubusercontent.com/41651716/227009612-9bc5fb72-2a44-4c55-9b7b-a0fa098e7f25.gif)

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3581](https://github.com/gradio-app/gradio/pull/3581).

- Trigger the release event when Slider number input is released or unfocused by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3589](https://github.com/gradio-app/gradio/pull/3589)

## Bug Fixes:

- Fixed bug where text for altair plots was not legible in dark mode by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3555](https://github.com/gradio-app/gradio/pull/3555)
- Fixes `Chatbot` and `Image` components so that files passed during processing are added to a directory where they can be served from, by [@abidlabs](https://github.com/abidlabs) in [PR 3523](https://github.com/gradio-app/gradio/pull/3523)
- Use Gradio API server to send telemetry using `huggingface_hub` [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3488](https://github.com/gradio-app/gradio/pull/3488)
- Fixes an an issue where if the Blocks scope was not exited, then State could be shared across sessions, by [@abidlabs](https://github.com/abidlabs) in [PR 3600](https://github.com/gradio-app/gradio/pull/3600)
- Ensures that `gr.load()` loads and applies the upstream theme, by [@abidlabs](https://github.com/abidlabs) in [PR 3641](https://github.com/gradio-app/gradio/pull/3641)
- Fixed bug where "or" was not being localized in file upload text by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3599](https://github.com/gradio-app/gradio/pull/3599)
- Fixed bug where chatbot does not autoscroll inside of a tab, row or column by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3637](https://github.com/gradio-app/gradio/pull/3637)
- Fixed bug where textbox shrinks when `lines` set to larger than 20 by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3637](https://github.com/gradio-app/gradio/pull/3637)
- Ensure CSS has fully loaded before rendering the application, by [@pngwn](https://github.com/pngwn) in [PR 3573](https://github.com/gradio-app/gradio/pull/3573)
- Support using an empty list as `gr.Dataframe` value, by [@space-nuko](https://github.com/space-nuko) in [PR 3646](https://github.com/gradio-app/gradio/pull/3646)
- Fixed `gr.Image` not filling the entire element size, by [@space-nuko](https://github.com/space-nuko) in [PR 3649](https://github.com/gradio-app/gradio/pull/3649)
- Make `gr.Code` support the `lines` property, by [@space-nuko](https://github.com/space-nuko) in [PR 3651](https://github.com/gradio-app/gradio/pull/3651)
- Fixes certain `_js` return values being double wrapped in an array, by [@space-nuko](https://github.com/space-nuko) in [PR 3594](https://github.com/gradio-app/gradio/pull/3594)
- Correct the documentation of `gr.File` component to state that its preprocessing method converts the uploaded file to a temporary file, by @RussellLuo in [PR 3660](https://github.com/gradio-app/gradio/pull/3660)
- Fixed bug in Serializer ValueError text by [@osanseviero](https://github.com/osanseviero) in [PR 3669](https://github.com/gradio-app/gradio/pull/3669)
- Fix default parameter argument and `gr.Progress` used in same function, by [@space-nuko](https://github.com/space-nuko) in [PR 3671](https://github.com/gradio-app/gradio/pull/3671)
- Hide `Remove All` button in `gr.Dropdown` single-select mode by [@space-nuko](https://github.com/space-nuko) in [PR 3678](https://github.com/gradio-app/gradio/pull/3678)
- Fix broken spaces in docs by [@aliabd](https://github.com/aliabd) in [PR 3698](https://github.com/gradio-app/gradio/pull/3698)
- Fix items in `gr.Dropdown` besides the selected item receiving a checkmark, by [@space-nuko](https://github.com/space-nuko) in [PR 3644](https://github.com/gradio-app/gradio/pull/3644)
- Fix several `gr.Dropdown` issues and improve usability, by [@space-nuko](https://github.com/space-nuko) in [PR 3705](https://github.com/gradio-app/gradio/pull/3705)

## Documentation Changes:

- Makes some fixes to the Theme Guide related to naming of variables, by [@abidlabs](https://github.com/abidlabs) in [PR 3561](https://github.com/gradio-app/gradio/pull/3561)
- Documented `HuggingFaceDatasetJSONSaver` by [@osanseviero](https://github.com/osanseviero) in [PR 3604](https://github.com/gradio-app/gradio/pull/3604)
- Makes some additions to documentation of `Audio` and `State` components, and fixes the `pictionary` demo by [@abidlabs](https://github.com/abidlabs) in [PR 3611](https://github.com/gradio-app/gradio/pull/3611)
- Fix outdated sharing your app guide by [@aliabd](https://github.com/aliabd) in [PR 3699](https://github.com/gradio-app/gradio/pull/3699)

## Testing and Infrastructure Changes:

- Removed heavily-mocked tests related to comet_ml, wandb, and mlflow as they added a significant amount of test dependencies that prevented installation of test dependencies on Windows environments. By [@abidlabs](https://github.com/abidlabs) in [PR 3608](https://github.com/gradio-app/gradio/pull/3608)
- Added Windows continuous integration, by [@space-nuko](https://github.com/space-nuko) in [PR 3628](https://github.com/gradio-app/gradio/pull/3628)
- Switched linting from flake8 + isort to `ruff`, by [@akx](https://github.com/akx) in [PR 3710](https://github.com/gradio-app/gradio/pull/3710)

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Mobile responsive iframes in themes guide by [@aliabd](https://github.com/aliabd) in [PR 3562](https://github.com/gradio-app/gradio/pull/3562)
- Remove extra $demo from theme guide by [@aliabd](https://github.com/aliabd) in [PR 3563](https://github.com/gradio-app/gradio/pull/3563)
- Set the theme name to be the upstream repo name when loading from the hub by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3595](https://github.com/gradio-app/gradio/pull/3595)
- Copy everything in website Dockerfile, fix build issues by [@aliabd](https://github.com/aliabd) in [PR 3659](https://github.com/gradio-app/gradio/pull/3659)
- Raise error when an event is queued but the queue is not configured by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3640](https://github.com/gradio-app/gradio/pull/3640)
- Allows users to apss in a string name for a built-in theme, by [@abidlabs](https://github.com/abidlabs) in [PR 3641](https://github.com/gradio-app/gradio/pull/3641)
- Added `orig_name` to Video output in the backend so that the front end can set the right name for downloaded video files by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3700](https://github.com/gradio-app/gradio/pull/3700)

## Contributors Shoutout:

No changes to highlight.

# Version 3.23.0

## New Features:

### Theme Sharing!

Once you have created a theme, you can upload it to the HuggingFace Hub to let others view it, use it, and build off of it! You can also download, reuse, and remix other peoples' themes. See https://gradio.app/theming-guide/ for more details.

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3428](https://github.com/gradio-app/gradio/pull/3428)

## Bug Fixes:

- Removes leading spaces from all lines of code uniformly in the `gr.Code()` component. By [@abidlabs](https://github.com/abidlabs) in [PR 3556](https://github.com/gradio-app/gradio/pull/3556)
- Fixed broken login page, by [@aliabid94](https://github.com/aliabid94) in [PR 3529](https://github.com/gradio-app/gradio/pull/3529)

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Fix rendering of dropdowns to take more space, and related bugs, by [@aliabid94](https://github.com/aliabid94) in [PR 3549](https://github.com/gradio-app/gradio/pull/3549)

## Contributors Shoutout:

No changes to highlight.

# Version 3.22.1

## New Features:

No changes to highlight.

## Bug Fixes:

- Restore label bars by [@aliabid94](https://github.com/aliabid94) in [PR 3507](https://github.com/gradio-app/gradio/pull/3507)

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.22.0

## New Features:

### Official Theme release

Gradio now supports a new theme system, which allows you to customize the look and feel of your app. You can now use the `theme=` kwarg to pass in a prebuilt theme, or customize your own! See https://gradio.app/theming-guide/ for more details. By [@aliabid94](https://github.com/aliabid94) in [PR 3470](https://github.com/gradio-app/gradio/pull/3470) and [PR 3497](https://github.com/gradio-app/gradio/pull/3497)

### `elem_classes`

Add keyword argument `elem_classes` to Components to control class names of components, in the same manner as existing `elem_id`.
By [@aliabid94](https://github.com/aliabid94) in [PR 3466](https://github.com/gradio-app/gradio/pull/3466)

## Bug Fixes:

- Fixes the File.upload() event trigger which broke as part of the change in how we uploaded files by [@abidlabs](https://github.com/abidlabs) in [PR 3462](https://github.com/gradio-app/gradio/pull/3462)
- Fixed issue with `gr.Request` object failing to handle dictionaries when nested keys couldn't be converted to variable names [#3454](https://github.com/gradio-app/gradio/issues/3454) by [@radames](https://github.com/radames) in [PR 3459](https://github.com/gradio-app/gradio/pull/3459)
- Fixed bug where css and client api was not working properly when mounted in a subpath by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3482](https://github.com/gradio-app/gradio/pull/3482)

## Documentation Changes:

- Document gr.Error in the docs by [@aliabd](https://github.com/aliabd) in [PR 3465](https://github.com/gradio-app/gradio/pull/3465)

## Testing and Infrastructure Changes:

- Pinned `pyright==1.1.298` for stability by [@abidlabs](https://github.com/abidlabs) in [PR 3475](https://github.com/gradio-app/gradio/pull/3475)
- Removed `IOComponent.add_interactive_to_config()` by [@space-nuko](https://github.com/space-nuko) in [PR 3476](https://github.com/gradio-app/gradio/pull/3476)
- Removed `IOComponent.generate_sample()` by [@space-nuko](https://github.com/space-nuko) in [PR 3475](https://github.com/gradio-app/gradio/pull/3483)

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Revert primary button background color in dark mode by [@aliabid94](https://github.com/aliabid94) in [PR 3468](https://github.com/gradio-app/gradio/pull/3468)

## Contributors Shoutout:

No changes to highlight.

# Version 3.21.0

## New Features:

### Theme Sharing 🎨 🤝

You can now share your gradio themes with the world!

After creating a theme, you can upload it to the HuggingFace Hub to let others view it, use it, and build off of it!

### Uploading

There are two ways to upload a theme, via the theme class instance or the command line.

1. Via the class instance

```python
my_theme.push_to_hub(repo_name="my_theme",
                     version="0.2.0",
                     hf_token="...")
```

2. Via the command line

First save the theme to disk

```python
my_theme.dump(filename="my_theme.json")
```

Then use the `upload_theme` command:

```bash
upload_theme\
"my_theme.json"\
"my_theme"\
"0.2.0"\
"<hf-token>"
```

The `version` must be a valid [semantic version](https://www.geeksforgeeks.org/introduction-semantic-versioning/) string.

This creates a space on the huggingface hub to host the theme files and show potential users a preview of your theme.

An example theme space is here: https://huggingface.co/spaces/freddyaboulton/dracula_revamped

### Downloading

To use a theme from the hub, use the `from_hub` method on the `ThemeClass` and pass it to your app:

```python
my_theme = gr.Theme.from_hub("freddyaboulton/my_theme")

with gr.Blocks(theme=my_theme) as demo:
    ....
```

You can also pass the theme string directly to `Blocks` or `Interface` (`gr.Blocks(theme="freddyaboulton/my_theme")`)

You can pin your app to an upstream theme version by using semantic versioning expressions.

For example, the following would ensure the theme we load from the `my_theme` repo was between versions `0.1.0` and `0.2.0`:

```python
with gr.Blocks(theme="freddyaboulton/my_theme@>=0.1.0,<0.2.0") as demo:
    ....
```

by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3428](https://github.com/gradio-app/gradio/pull/3428)

### Code component 🦾

New code component allows you to enter, edit and display code with full syntax highlighting by [@pngwn](https://github.com/pngwn) in [PR 3421](https://github.com/gradio-app/gradio/pull/3421)

### The `Chatbot` component now supports audio, video, and images

The `Chatbot` component now supports audio, video, and images with a simple syntax: simply
pass in a tuple with the URL or filepath (the second optional element of the tuple is alt text), and the image/audio/video will be displayed:

```python
gr.Chatbot([
    (("driving.mp4",), "cool video"),
    (("cantina.wav",), "cool audio"),
    (("lion.jpg", "A lion"), "cool pic"),
]).style(height=800)
```

<img width="1054" alt="image" src="https://user-images.githubusercontent.com/1778297/224116682-5908db47-f0fa-405c-82ab-9c7453e8c4f1.png">

Note: images were previously supported via Markdown syntax and that is still supported for backwards compatibility. By [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3413](https://github.com/gradio-app/gradio/pull/3413)

- Allow consecutive function triggers with `.then` and `.success` by [@aliabid94](https://github.com/aliabid94) in [PR 3430](https://github.com/gradio-app/gradio/pull/3430)

- New code component allows you to enter, edit and display code with full syntax highlighting by [@pngwn](https://github.com/pngwn) in [PR 3421](https://github.com/gradio-app/gradio/pull/3421)

![](https://user-images.githubusercontent.com/12937446/224116643-5cfb94b3-93ce-43ee-bb7b-c25c3b66e0a1.png)

- Added the `.select()` event listener, which also includes event data that can be passed as an argument to a function with type hint `gr.SelectData`. The following components support the `.select()` event listener: Chatbot, CheckboxGroup, Dataframe, Dropdown, File, Gallery, HighlightedText, Label, Radio, TabItem, Tab, Textbox. Example usage:

```python
import gradio as gr

with gr.Blocks() as demo:
    gallery = gr.Gallery(["images/1.jpg", "images/2.jpg", "images/3.jpg"])
    selected_index = gr.Textbox()

    def on_select(evt: gr.SelectData):
        return evt.index

    gallery.select(on_select, None, selected_index)
```

By [@aliabid94](https://github.com/aliabid94) in [PR 3399](https://github.com/gradio-app/gradio/pull/3399)

- The `Textbox` component now includes a copy button by [@abidlabs](https://github.com/abidlabs) in [PR 3452](https://github.com/gradio-app/gradio/pull/3452)

## Bug Fixes:

- Use `huggingface_hub` to send telemetry on `interface` and `blocks`; eventually to replace segment by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3342](https://github.com/gradio-app/gradio/pull/3342)
- Ensure load events created by components (randomize for slider, callable values) are never queued unless every is passed by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3391](https://github.com/gradio-app/gradio/pull/3391)
- Prevent in-place updates of `generic_update` by shallow copying by [@gitgithan](https://github.com/gitgithan) in [PR 3405](https://github.com/gradio-app/gradio/pull/3405) to fix [#3282](https://github.com/gradio-app/gradio/issues/3282)
- Fix bug caused by not importing `BlockContext` in `utils.py` by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3424](https://github.com/gradio-app/gradio/pull/3424)
- Ensure dropdown does not highlight partial matches by [@pngwn](https://github.com/pngwn) in [PR 3421](https://github.com/gradio-app/gradio/pull/3421)
- Fix mic button display by [@aliabid94](https://github.com/aliabid94) in [PR 3456](https://github.com/gradio-app/gradio/pull/3456)

## Documentation Changes:

- Added a section on security and access when sharing Gradio apps by [@abidlabs](https://github.com/abidlabs) in [PR 3408](https://github.com/gradio-app/gradio/pull/3408)
- Add Chinese README by [@uanu2002](https://github.com/uanu2002) in [PR 3394](https://github.com/gradio-app/gradio/pull/3394)
- Adds documentation for web components by [@abidlabs](https://github.com/abidlabs) in [PR 3407](https://github.com/gradio-app/gradio/pull/3407)
- Fixed link in Chinese readme by [@eltociear](https://github.com/eltociear) in [PR 3417](https://github.com/gradio-app/gradio/pull/3417)
- Document Blocks methods by [@aliabd](https://github.com/aliabd) in [PR 3427](https://github.com/gradio-app/gradio/pull/3427)
- Fixed bug where event handlers were not showing up in documentation by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3434](https://github.com/gradio-app/gradio/pull/3434)

## Testing and Infrastructure Changes:

- Fixes tests that were failing locally but passing on CI by [@abidlabs](https://github.com/abidlabs) in [PR 3411](https://github.com/gradio-app/gradio/pull/3411)
- Remove codecov from the repo by [@aliabd](https://github.com/aliabd) in [PR 3415](https://github.com/gradio-app/gradio/pull/3415)

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Prevent in-place updates of `generic_update` by shallow copying by [@gitgithan](https://github.com/gitgithan) in [PR 3405](https://github.com/gradio-app/gradio/pull/3405) to fix [#3282](https://github.com/gradio-app/gradio/issues/3282)
- Persist file names of files uploaded through any Gradio component by [@abidlabs](https://github.com/abidlabs) in [PR 3412](https://github.com/gradio-app/gradio/pull/3412)
- Fix markdown embedded component in docs by [@aliabd](https://github.com/aliabd) in [PR 3410](https://github.com/gradio-app/gradio/pull/3410)
- Clean up event listeners code by [@aliabid94](https://github.com/aliabid94) in [PR 3420](https://github.com/gradio-app/gradio/pull/3420)
- Fix css issue with spaces logo by [@aliabd](https://github.com/aliabd) in [PR 3422](https://github.com/gradio-app/gradio/pull/3422)
- Makes a few fixes to the `JSON` component (show_label parameter, icons) in [@abidlabs](https://github.com/abidlabs) in [PR 3451](https://github.com/gradio-app/gradio/pull/3451)

## Contributors Shoutout:

No changes to highlight.

# Version 3.20.1

## New Features:

- Add `height` kwarg to style in `gr.Chatbot()` component by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3369](https://github.com/gradio-app/gradio/pull/3369)

```python
chatbot = gr.Chatbot().style(height=500)
```

## Bug Fixes:

- Ensure uploaded images are always shown in the sketch tool by [@pngwn](https://github.com/pngwn) in [PR 3386](https://github.com/gradio-app/gradio/pull/3386)
- Fixes bug where when if fn is a non-static class member, then self should be ignored as the first param of the fn by [@or25](https://github.com/or25) in [PR #3227](https://github.com/gradio-app/gradio/pull/3227)

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.20.0

## New Features:

### Release event for Slider

Now you can trigger your python function to run when the slider is released as opposed to every slider change value!

Simply use the `release` method on the slider

```python
slider.release(function, inputs=[...], outputs=[...], api_name="predict")
```

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3353](https://github.com/gradio-app/gradio/pull/3353)

### Dropdown Component Updates

The standard dropdown component now supports searching for choices. Also when `multiselect` is `True`, you can specify `max_choices` to set the maximum number of choices you want the user to be able to select from the dropdown component.

```python
gr.Dropdown(label="Choose your favorite colors", choices=["red", "blue", "green", "yellow", "orange"], multiselect=True, max_choices=2)
```

by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3211](https://github.com/gradio-app/gradio/pull/3211)

### Download button for images 🖼️

Output images will now automatically have a download button displayed to make it easier to save and share
the results of Machine Learning art models.

![download_sketch](https://user-images.githubusercontent.com/41651716/221025113-e693bf41-eabd-42b3-a4f2-26f2708d98fe.gif)

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3297](https://github.com/gradio-app/gradio/pull/3297)

- Updated image upload component to accept all image formats, including lossless formats like .webp by [@fienestar](https://github.com/fienestar) in [PR 3225](https://github.com/gradio-app/gradio/pull/3225)
- Adds a disabled mode to the `gr.Button` component by setting `interactive=False` by [@abidlabs](https://github.com/abidlabs) in [PR 3266](https://github.com/gradio-app/gradio/pull/3266) and [PR 3288](https://github.com/gradio-app/gradio/pull/3288)
- Adds visual feedback to the when the Flag button is clicked, by [@abidlabs](https://github.com/abidlabs) in [PR 3289](https://github.com/gradio-app/gradio/pull/3289)
- Adds ability to set `flagging_options` display text and saved flag separately by [@abidlabs](https://github.com/abidlabs) in [PR 3289](https://github.com/gradio-app/gradio/pull/3289)
- Allow the setting of `brush_radius` for the `Image` component both as a default and via `Image.update()` by [@pngwn](https://github.com/pngwn) in [PR 3277](https://github.com/gradio-app/gradio/pull/3277)
- Added `info=` argument to form components to enable extra context provided to users, by [@aliabid94](https://github.com/aliabid94) in [PR 3291](https://github.com/gradio-app/gradio/pull/3291)
- Allow developers to access the username of a logged-in user from the `gr.Request()` object using the `.username` attribute by [@abidlabs](https://github.com/abidlabs) in [PR 3296](https://github.com/gradio-app/gradio/pull/3296)
- Add `preview` option to `Gallery.style` that launches the gallery in preview mode when first loaded by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3345](https://github.com/gradio-app/gradio/pull/3345)

## Bug Fixes:

- Ensure `mirror_webcam` is always respected by [@pngwn](https://github.com/pngwn) in [PR 3245](https://github.com/gradio-app/gradio/pull/3245)
- Fix issue where updated markdown links were not being opened in a new tab by [@gante](https://github.com/gante) in [PR 3236](https://github.com/gradio-app/gradio/pull/3236)
- API Docs Fixes by [@aliabd](https://github.com/aliabd) in [PR 3287](https://github.com/gradio-app/gradio/pull/3287)
- Added a timeout to queue messages as some demos were experiencing infinitely growing queues from active jobs waiting forever for clients to respond by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3196](https://github.com/gradio-app/gradio/pull/3196)
- Fixes the height of rendered LaTeX images so that they match the height of surrounding text by [@abidlabs](https://github.com/abidlabs) in [PR 3258](https://github.com/gradio-app/gradio/pull/3258) and in [PR 3276](https://github.com/gradio-app/gradio/pull/3276)
- Fix bug where matplotlib images where always too small on the front end by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3274](https://github.com/gradio-app/gradio/pull/3274)
- Remove embed's `initial_height` when loading is complete so the embed finds its natural height once it is loaded [@pngwn](https://github.com/pngwn) in [PR 3292](https://github.com/gradio-app/gradio/pull/3292)
- Prevent Sketch from crashing when a default image is provided by [@pngwn](https://github.com/pngwn) in [PR 3277](https://github.com/gradio-app/gradio/pull/3277)
- Respect the `shape` argument on the front end when creating Image Sketches by [@pngwn](https://github.com/pngwn) in [PR 3277](https://github.com/gradio-app/gradio/pull/3277)
- Fix infinite loop caused by setting `Dropdown's` value to be `[]` and adding a change event on the dropdown by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3295](https://github.com/gradio-app/gradio/pull/3295)
- Fix change event listed twice in image docs by [@aliabd](https://github.com/aliabd) in [PR 3318](https://github.com/gradio-app/gradio/pull/3318)
- Fix bug that cause UI to be vertically centered at all times by [@pngwn](https://github.com/pngwn) in [PR 3336](https://github.com/gradio-app/gradio/pull/3336)
- Fix bug where `height` set in `Gallery.style` was not respected by the front-end by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3343](https://github.com/gradio-app/gradio/pull/3343)
- Ensure markdown lists are rendered correctly by [@pngwn](https://github.com/pngwn) in [PR 3341](https://github.com/gradio-app/gradio/pull/3341)
- Ensure that the initial empty value for `gr.Dropdown(Multiselect=True)` is an empty list and the initial value for `gr.Dropdown(Multiselect=False)` is an empty string by [@pngwn](https://github.com/pngwn) in [PR 3338](https://github.com/gradio-app/gradio/pull/3338)
- Ensure uploaded images respect the shape property when the canvas is also enabled by [@pngwn](https://github.com/pngwn) in [PR 3351](https://github.com/gradio-app/gradio/pull/3351)
- Ensure that Google Analytics works correctly when gradio apps are created with `analytics_enabled=True` by [@abidlabs](https://github.com/abidlabs) in [PR 3349](https://github.com/gradio-app/gradio/pull/3349)
- Fix bug where files were being re-uploaded after updates by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3375](https://github.com/gradio-app/gradio/pull/3375)
- Fix error when using backen_fn and custom js at the same time by [@jialeicui](https://github.com/jialeicui) in [PR 3358](https://github.com/gradio-app/gradio/pull/3358)
- Support new embeds for huggingface spaces subdomains by [@pngwn](https://github.com/pngwn) in [PR 3367](https://github.com/gradio-app/gradio/pull/3367)

## Documentation Changes:

- Added the `types` field to the dependency field in the config by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3315](https://github.com/gradio-app/gradio/pull/3315)
- Gradio Status Page by [@aliabd](https://github.com/aliabd) in [PR 3331](https://github.com/gradio-app/gradio/pull/3331)
- Adds a Guide on setting up a dashboard from Supabase data using the `gr.BarPlot`
  component by [@abidlabs](https://github.com/abidlabs) in [PR 3275](https://github.com/gradio-app/gradio/pull/3275)

## Testing and Infrastructure Changes:

- Adds a script to benchmark the performance of the queue and adds some instructions on how to use it. By [@freddyaboulton](https://github.com/freddyaboulton) and [@abidlabs](https://github.com/abidlabs) in [PR 3272](https://github.com/gradio-app/gradio/pull/3272)
- Flaky python tests no longer cancel non-flaky tests by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3344](https://github.com/gradio-app/gradio/pull/3344)

## Breaking Changes:

- Chatbot bubble colors can no longer be set by `chatbot.style(color_map=)` by [@aliabid94] in [PR 3370](https://github.com/gradio-app/gradio/pull/3370)

## Full Changelog:

- Fixed comment typo in components.py by [@eltociear](https://github.com/eltociear) in [PR 3235](https://github.com/gradio-app/gradio/pull/3235)
- Cleaned up chatbot ui look and feel by [@aliabid94] in [PR 3370](https://github.com/gradio-app/gradio/pull/3370)

## Contributors Shoutout:

No changes to highlight.

# Version 3.19.1

## New Features:

No changes to highlight.

## Bug Fixes:

- UI fixes including footer and API docs by [@aliabid94](https://github.com/aliabid94) in [PR 3242](https://github.com/gradio-app/gradio/pull/3242)
- Updated image upload component to accept all image formats, including lossless formats like .webp by [@fienestar](https://github.com/fienestar) in [PR 3225](https://github.com/gradio-app/gradio/pull/3225)

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Added backend support for themes by [@aliabid94](https://github.com/aliabid94) in [PR 2931](https://github.com/gradio-app/gradio/pull/2931)
- Added support for button sizes "lg" (default) and "sm".

## Contributors Shoutout:

No changes to highlight.

# Version 3.19.0

## New Features:

### Improved embedding experience

When embedding a spaces-hosted gradio app as a web component, you now get an improved UI linking back to the original space, better error handling and more intelligent load performance. No changes are required to your code to benefit from this enhanced experience; simply upgrade your gradio SDK to the latest version.

![](https://user-images.githubusercontent.com/12937446/219653294-86937632-72c1-4e93-a77c-af705d49382a.png)

This behaviour is configurable. You can disable the info panel at the bottom by passing `info="false"`. You can disable the container entirely by passing `container="false"`.

Error statuses are reported in the UI with an easy way for end-users to report problems to the original space author via the community tab of that Hugginface space:

![](https://user-images.githubusercontent.com/12937446/219655499-88019443-d694-44e7-9e6d-242e19d10a5c.png)

By default, gradio apps are lazy loaded, vastly improving performance when there are several demos on the page. Metadata is loaded ahead of time, but the space will only be loaded and rendered when it is in view.

This behaviour is configurable. You can pass `eager="true"` to load and render the space regardless of whether or not it is currently on the screen.

by [@pngwn](https://github.com/pngwn) in [PR 3205](https://github.com/gradio-app/gradio/pull/3205)

### New `gr.BarPlot` component! 📊

Create interactive bar plots from a high-level interface with `gr.BarPlot`.
No need to remember matplotlib syntax anymore!

Example usage:

```python
import gradio as gr
import pandas as pd

simple = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

with gr.Blocks() as demo:
    gr.BarPlot(
        simple,
        x="a",
        y="b",
        title="Simple Bar Plot with made up data",
        tooltip=['a', 'b'],
    )

demo.launch()
```

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3157](https://github.com/gradio-app/gradio/pull/3157)

### Bokeh plots are back! 🌠

Fixed a bug that prevented bokeh plots from being displayed on the front end and extended support for both 2.x and 3.x versions of bokeh!

![image](https://user-images.githubusercontent.com/41651716/219468324-0d82e07f-8fb4-4ff9-b40c-8250b29e45f7.png)

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3212](https://github.com/gradio-app/gradio/pull/3212)

## Bug Fixes:

- Adds ability to add a single message from the bot or user side. Ex: specify `None` as the second value in the tuple, to add a single message in the chatbot from the "bot" side.

```python
gr.Chatbot([("Hi, I'm DialoGPT. Try asking me a question.", None)])
```

By [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3165](https://github.com/gradio-app/gradio/pull/3165)

- Fixes `gr.utils.delete_none` to only remove props whose values are `None` from the config by [@abidlabs](https://github.com/abidlabs) in [PR 3188](https://github.com/gradio-app/gradio/pull/3188)
- Fix bug where embedded demos were not loading files properly by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3177](https://github.com/gradio-app/gradio/pull/3177)
- The `change` event is now triggered when users click the 'Clear All' button of the multiselect DropDown component by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3195](https://github.com/gradio-app/gradio/pull/3195)
- Stops File component from freezing when a large file is uploaded by [@aliabid94](https://github.com/aliabid94) in [PR 3191](https://github.com/gradio-app/gradio/pull/3191)
- Support Chinese pinyin in Dataframe by [@aliabid94](https://github.com/aliabid94) in [PR 3206](https://github.com/gradio-app/gradio/pull/3206)
- The `clear` event is now triggered when images are cleared by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3218](https://github.com/gradio-app/gradio/pull/3218)
- Fix bug where auth cookies where not sent when connecting to an app via http by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3223](https://github.com/gradio-app/gradio/pull/3223)
- Ensure latext CSS is always applied in light and dark mode by [@pngwn](https://github.com/pngwn) in [PR 3233](https://github.com/gradio-app/gradio/pull/3233)

## Documentation Changes:

- Sort components in docs by alphabetic order by [@aliabd](https://github.com/aliabd) in [PR 3152](https://github.com/gradio-app/gradio/pull/3152)
- Changes to W&B guide by [@scottire](https://github.com/scottire) in [PR 3153](https://github.com/gradio-app/gradio/pull/3153)
- Keep pnginfo metadata for gallery by [@wfng92](https://github.com/wfng92) in [PR 3150](https://github.com/gradio-app/gradio/pull/3150)
- Add a section on how to run a Gradio app locally [@osanseviero](https://github.com/osanseviero) in [PR 3170](https://github.com/gradio-app/gradio/pull/3170)
- Fixed typos in gradio events function documentation by [@vidalmaxime](https://github.com/vidalmaxime) in [PR 3168](https://github.com/gradio-app/gradio/pull/3168)
- Added an example using Gradio's batch mode with the diffusers library by [@abidlabs](https://github.com/abidlabs) in [PR 3224](https://github.com/gradio-app/gradio/pull/3224)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Fix demos page css and add close demos button by [@aliabd](https://github.com/aliabd) in [PR 3151](https://github.com/gradio-app/gradio/pull/3151)
- Caches temp files from base64 input data by giving them a deterministic path based on the contents of data by [@abidlabs](https://github.com/abidlabs) in [PR 3197](https://github.com/gradio-app/gradio/pull/3197)
- Better warnings (when there is a mismatch between the number of output components and values returned by a function, or when the `File` component or `UploadButton` component includes a `file_types` parameter along with `file_count=="dir"`) by [@abidlabs](https://github.com/abidlabs) in [PR 3194](https://github.com/gradio-app/gradio/pull/3194)
- Raises a `gr.Error` instead of a regular Python error when you use `gr.Interface.load()` to load a model and there's an error querying the HF API by [@abidlabs](https://github.com/abidlabs) in [PR 3194](https://github.com/gradio-app/gradio/pull/3194)
- Fixed gradio share links so that they are persistent and do not reset if network
  connection is disrupted by by [XciD](https://github.com/XciD), [Wauplin](https://github.com/Wauplin), and [@abidlabs](https://github.com/abidlabs) in [PR 3149](https://github.com/gradio-app/gradio/pull/3149) and a follow-up to allow it to work for users upgrading from a previous Gradio version in [PR 3221](https://github.com/gradio-app/gradio/pull/3221)

## Contributors Shoutout:

No changes to highlight.

# Version 3.18.0

## New Features:

### Revamped Stop Button for Interfaces 🛑

If your Interface function is a generator, there used to be a separate `Stop` button displayed next
to the `Submit` button.

We've revamed the `Submit` button so that it turns into a `Stop` button during the generation process.
Clicking on the `Stop` button will cancel the generation and turn it back to a `Submit` button.
The `Stop` button will automatically turn back to a `Submit` button at the end of the generation if you don't use it!

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3124](https://github.com/gradio-app/gradio/pull/3124)

### Queue now works with reload mode!

You can now call `queue` on your `demo` outside of the `if __name__ == "__main__"` block and
run the script in reload mode with the `gradio` command.

Any changes to the `app.py` file will be reflected in the webpage automatically and the queue will work
properly!

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3089](https://github.com/gradio-app/gradio/pull/3089)

### Allow serving files from additional directories

```python
demo = gr.Interface(...)
demo.launch(
  file_directories=["/var/lib/demo/path/to/resources"]
)
```

By [@maxaudron](https://github.com/maxaudron) in [PR 3075](https://github.com/gradio-app/gradio/pull/3075)

## Bug Fixes:

- Fixes URL resolution on Windows by [@abidlabs](https://github.com/abidlabs) in [PR 3108](https://github.com/gradio-app/gradio/pull/3108)
- Example caching now works with components without a label attribute (e.g. `Column`) by [@abidlabs](https://github.com/abidlabs) in [PR 3123](https://github.com/gradio-app/gradio/pull/3123)
- Ensure the Video component correctly resets the UI state when a new video source is loaded and reduce choppiness of UI by [@pngwn](https://github.com/abidlabs) in [PR 3117](https://github.com/gradio-app/gradio/pull/3117)
- Fixes loading private Spaces by [@abidlabs](https://github.com/abidlabs) in [PR 3068](https://github.com/gradio-app/gradio/pull/3068)
- Added a warning when attempting to launch an `Interface` via the `%%blocks` jupyter notebook magic command by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3126](https://github.com/gradio-app/gradio/pull/3126)
- Fixes bug where interactive output image cannot be set when in edit mode by [@dawoodkhan82](https://github.com/@dawoodkhan82) in [PR 3135](https://github.com/gradio-app/gradio/pull/3135)
- A share link will automatically be created when running on Sagemaker notebooks so that the front-end is properly displayed by [@abidlabs](https://github.com/abidlabs) in [PR 3137](https://github.com/gradio-app/gradio/pull/3137)
- Fixes a few dropdown component issues; hide checkmark next to options as expected, and keyboard hover is visible by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3145]https://github.com/gradio-app/gradio/pull/3145)
- Fixed bug where example pagination buttons were not visible in dark mode or displayed under the examples table. By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3144](https://github.com/gradio-app/gradio/pull/3144)
- Fixed bug where the font color of axis labels and titles for native plots did not respond to dark mode preferences. By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3146](https://github.com/gradio-app/gradio/pull/3146)

## Documentation Changes:

- Added a guide on the 4 kinds of Gradio Interfaces by [@yvrjsharma](https://github.com/yvrjsharma) and [@abidlabs](https://github.com/abidlabs) in [PR 3003](https://github.com/gradio-app/gradio/pull/3003)
- Explained that the parameters in `launch` will not be respected when using reload mode, e.g. `gradio` command by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3089](https://github.com/gradio-app/gradio/pull/3089)
- Added a demo to show how to set up variable numbers of outputs in Gradio by [@abidlabs](https://github.com/abidlabs) in [PR 3127](https://github.com/gradio-app/gradio/pull/3127)
- Updated docs to reflect that the `equal_height` parameter should be passed to the `.style()` method of `gr.Row()` by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3125](https://github.com/gradio-app/gradio/pull/3125)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Changed URL of final image for `fake_diffusion` demos by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3120](https://github.com/gradio-app/gradio/pull/3120)

## Contributors Shoutout:

No changes to highlight.

# Version 3.17.1

## New Features:

### iOS image rotation fixed 🔄

Previously photos uploaded via iOS would be rotated after processing. This has been fixed by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3089](https://github.com/gradio-app/gradio/pull/3091)

#### Before

![image](https://user-images.githubusercontent.com/41651716/215846507-a36e9d05-1ac2-4867-8ab3-ce045a9415d9.png)

#### After

![image](https://user-images.githubusercontent.com/41651716/215846554-e41773ed-70f0-491a-9952-6a18babf91ef.png)

### Run on Kaggle kernels 🧪

A share link will automatically be created when running on Kaggle kernels (notebooks) so that the front-end is properly displayed.

![image](https://user-images.githubusercontent.com/41651716/216104254-2cf55599-449c-436c-b57e-40f6a83f9eee.png)

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3101](https://github.com/gradio-app/gradio/pull/3101)

## Bug Fixes:

- Fix bug where examples were not rendered correctly for demos created with Blocks api that had multiple input compinents by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3090](https://github.com/gradio-app/gradio/pull/3090)
- Fix change event listener for JSON, HighlightedText, Chatbot by [@aliabid94](https://github.com/aliabid94) in [PR 3095](https://github.com/gradio-app/gradio/pull/3095)
- Fixes bug where video and file change event not working [@tomchang25](https://github.com/tomchang25) in [PR 3098](https://github.com/gradio-app/gradio/pull/3098)
- Fixes bug where static_video play and pause event not working [@tomchang25](https://github.com/tomchang25) in [PR 3098](https://github.com/gradio-app/gradio/pull/3098)
- Fixed `Gallery.style(grid=...)` by by [@aliabd](https://github.com/aliabd) in [PR 3107](https://github.com/gradio-app/gradio/pull/3107)

## Documentation Changes:

- Update chatbot guide to include blocks demo and markdown support section by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3023](https://github.com/gradio-app/gradio/pull/3023)

* Fix a broken link in the Quick Start guide, by [@cakiki](https://github.com/cakiki) in [PR 3109](https://github.com/gradio-app/gradio/pull/3109)
* Better docs navigation on mobile by [@aliabd](https://github.com/aliabd) in [PR 3112](https://github.com/gradio-app/gradio/pull/3112)
* Add a guide on using Gradio with [Comet](https://comet.com/), by [@DN6](https://github.com/DN6/) in [PR 3058](https://github.com/gradio-app/gradio/pull/3058)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Set minimum `markdown-it-py` version to `2.0.0` so that the dollar math plugin is compatible by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3102](https://github.com/gradio-app/gradio/pull/3102)

## Contributors Shoutout:

No changes to highlight.

# Version 3.17.0

## New Features:

### Extended support for Interface.load! 🏗️

You can now load `image-to-text` and `conversational` pipelines from the hub!

### Image-to-text Demo

```python
io = gr.Interface.load("models/nlpconnect/vit-gpt2-image-captioning",
                       api_key="<optional-api-key>")
io.launch()
```

<img width="1087" alt="image" src="https://user-images.githubusercontent.com/41651716/213260197-dc5d80b4-6e50-4b3a-a764-94980930ac38.png">

### conversational Demo

```python
chatbot = gr.Interface.load("models/microsoft/DialoGPT-medium",
                           api_key="<optional-api-key>")
chatbot.launch()
```

![chatbot_load](https://user-images.githubusercontent.com/41651716/213260220-3eaa25b7-a38b-48c6-adeb-2718bdf297a2.gif)

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3011](https://github.com/gradio-app/gradio/pull/3011)

### Download Button added to Model3D Output Component 📥

No need for an additional file output component to enable model3d file downloads anymore. We now added a download button to the model3d component itself.

<img width="739" alt="Screenshot 2023-01-18 at 3 52 45 PM" src="https://user-images.githubusercontent.com/12725292/213294198-5f4fda35-bde7-450c-864f-d5683e7fa29a.png">

By [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3014](https://github.com/gradio-app/gradio/pull/3014)

### Fixing Auth on Spaces 🔑

Authentication on spaces works now! Third party cookies must be enabled on your browser to be able
to log in. Some browsers disable third party cookies by default (Safari, Chrome Incognito).

![auth_spaces](https://user-images.githubusercontent.com/41651716/215528417-09538933-0576-4d1d-b3b9-1e877ab01905.gif)

## Bug Fixes:

- Fixes bug where interpretation event was not configured correctly by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2993](https://github.com/gradio-app/gradio/pull/2993)
- Fix relative import bug in reload mode by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2992](https://github.com/gradio-app/gradio/pull/2992)
- Fixes bug where png files were not being recognized when uploading images by [@abidlabs](https://github.com/abidlabs) in [PR 3002](https://github.com/gradio-app/gradio/pull/3002)
- Fixes bug where external Spaces could not be loaded and used as functions if they returned files by [@abidlabs](https://github.com/abidlabs) in [PR 3004](https://github.com/gradio-app/gradio/pull/3004)
- Fix bug where file serialization output was not JSON serializable by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2999](https://github.com/gradio-app/gradio/pull/2999)
- Fixes bug where png files were not being recognized when uploading images by [@abidlabs](https://github.com/abidlabs) in [PR 3002](https://github.com/gradio-app/gradio/pull/3002)
- Fixes bug where temporary uploaded files were not being added to temp sets by [@abidlabs](https://github.com/abidlabs) in [PR 3005](https://github.com/gradio-app/gradio/pull/3005)
- Fixes issue where markdown support in chatbot breaks older demos [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3006](https://github.com/gradio-app/gradio/pull/3006)
- Fixes the `/file/` route that was broken in a recent change in [PR 3010](https://github.com/gradio-app/gradio/pull/3010)
- Fix bug where the Image component could not serialize image urls by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2957](https://github.com/gradio-app/gradio/pull/2957)
- Fix forwarding for guides after SEO renaming by [@aliabd](https://github.com/aliabd) in [PR 3017](https://github.com/gradio-app/gradio/pull/3017)
- Switch all pages on the website to use latest stable gradio by [@aliabd](https://github.com/aliabd) in [PR 3016](https://github.com/gradio-app/gradio/pull/3016)
- Fix bug related to deprecated parameters in `huggingface_hub` for the HuggingFaceDatasetSaver in [PR 3025](https://github.com/gradio-app/gradio/pull/3025)
- Added better support for symlinks in the way absolute paths are resolved by [@abidlabs](https://github.com/abidlabs) in [PR 3037](https://github.com/gradio-app/gradio/pull/3037)
- Fix several minor frontend bugs (loading animation, examples as gallery) frontend [@aliabid94](https://github.com/3026) in [PR 2961](https://github.com/gradio-app/gradio/pull/3026).
- Fixes bug that the chatbot sample code does not work with certain input value by [@petrov826](https://github.com/petrov826) in [PR 3039](https://github.com/gradio-app/gradio/pull/3039).
- Fix shadows for form element and ensure focus styles more visible in dark mode [@pngwn](https://github.com/pngwn) in [PR 3042](https://github.com/gradio-app/gradio/pull/3042).
- Fixed bug where the Checkbox and Dropdown change events were not triggered in response to other component changes by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3045](https://github.com/gradio-app/gradio/pull/3045)
- Fix bug where the queue was not properly restarted after launching a `closed` app by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3022](https://github.com/gradio-app/gradio/pull/3022)
- Adding missing embedded components on docs by [@aliabd](https://github.com/aliabd) in [PR 3027](https://github.com/gradio-app/gradio/pull/3027)
- Fixes bug where app would crash if the `file_types` parameter of `gr.File` or `gr.UploadButton` was not a list by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3048](https://github.com/gradio-app/gradio/pull/3048)
- Ensure CSS mounts correctly regardless of how many Gradio instances are on the page [@pngwn](https://github.com/pngwn) in [PR 3059](https://github.com/gradio-app/gradio/pull/3059).
- Fix bug where input component was not hidden in the frontend for `UploadButton` by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3053](https://github.com/gradio-app/gradio/pull/3053)
- Fixes issue where after clicking submit or undo, the sketch output wouldn't clear. [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 3047](https://github.com/gradio-app/gradio/pull/3047)
- Ensure spaces embedded via the web component always use the correct URLs for server requests and change ports for testing to avoid strange collisions when users are working with embedded apps locally by [@pngwn](https://github.com/pngwn) in [PR 3065](https://github.com/gradio-app/gradio/pull/3065)
- Preserve selected image of Gallery through updated by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3061](https://github.com/gradio-app/gradio/pull/3061)
- Fix bug where auth was not respected on HF spaces by [@freddyaboulton](https://github.com/freddyaboulton) and [@aliabid94](https://github.com/aliabid94) in [PR 3049](https://github.com/gradio-app/gradio/pull/3049)
- Fixes bug where tabs selected attribute not working if manually change tab by [@tomchang25](https://github.com/tomchang25) in [3055](https://github.com/gradio-app/gradio/pull/3055)
- Change chatbot to show dots on progress, and fix bug where chatbot would not stick to bottom in the case of images by [@aliabid94](https://github.com/aliabid94) in [PR 3067](https://github.com/gradio-app/gradio/pull/3079)

## Documentation Changes:

- SEO improvements to guides by[@aliabd](https://github.com/aliabd) in [PR 2915](https://github.com/gradio-app/gradio/pull/2915)
- Use `gr.LinePlot` for the `blocks_kinematics` demo by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2998](https://github.com/gradio-app/gradio/pull/2998)
- Updated the `interface_series_load` to include some inline markdown code by [@abidlabs](https://github.com/abidlabs) in [PR 3051](https://github.com/gradio-app/gradio/pull/3051)

## Testing and Infrastructure Changes:

- Adds a GitHub action to test if any large files (> 5MB) are present by [@abidlabs](https://github.com/abidlabs) in [PR 3013](https://github.com/gradio-app/gradio/pull/3013)

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Rewrote frontend using CSS variables for themes by [@pngwn](https://github.com/pngwn) in [PR 2840](https://github.com/gradio-app/gradio/pull/2840)
- Moved telemetry requests to run on background threads by [@abidlabs](https://github.com/abidlabs) in [PR 3054](https://github.com/gradio-app/gradio/pull/3054)

## Contributors Shoutout:

No changes to highlight.

# Version 3.16.2

## New Features:

No changes to highlight.

## Bug Fixes:

- Fixed file upload fails for files with zero size by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2923](https://github.com/gradio-app/gradio/pull/2923)
- Fixed bug where `mount_gradio_app` would not launch if the queue was enabled in a gradio app by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2939](https://github.com/gradio-app/gradio/pull/2939)
- Fix custom long CSS handling in Blocks by [@anton-l](https://github.com/anton-l) in [PR 2953](https://github.com/gradio-app/gradio/pull/2953)
- Recovers the dropdown change event by [@abidlabs](https://github.com/abidlabs) in [PR 2954](https://github.com/gradio-app/gradio/pull/2954).
- Fix audio file output by [@aliabid94](https://github.com/aliabid94) in [PR 2961](https://github.com/gradio-app/gradio/pull/2961).
- Fixed bug where file extensions of really long files were not kept after download by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2929](https://github.com/gradio-app/gradio/pull/2929)
- Fix bug where outputs for examples where not being returned by the backend by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2955](https://github.com/gradio-app/gradio/pull/2955)
- Fix bug in `blocks_plug` demo that prevented switching tabs programmatically with python [@TashaSkyUp](https://github.com/https://github.com/TashaSkyUp) in [PR 2971](https://github.com/gradio-app/gradio/pull/2971).

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.16.1

## New Features:

No changes to highlight.

## Bug Fixes:

- Fix audio file output by [@aliabid94](https://github.com/aliabid94) in [PR 2950](https://github.com/gradio-app/gradio/pull/2950).

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.16.0

## New Features:

### Send custom progress updates by adding a `gr.Progress` argument after the input arguments to any function. Example:

```python
def reverse(word, progress=gr.Progress()):
    progress(0, desc="Starting")
    time.sleep(1)
    new_string = ""
    for letter in progress.tqdm(word, desc="Reversing"):
        time.sleep(0.25)
        new_string = letter + new_string
    return new_string

demo = gr.Interface(reverse, gr.Text(), gr.Text())
```

Progress indicator bar by [@aliabid94](https://github.com/aliabid94) in [PR 2750](https://github.com/gradio-app/gradio/pull/2750).

- Added `title` argument to `TabbedInterface` by @MohamedAliRashad in [#2888](https://github.com/gradio-app/gradio/pull/2888)
- Add support for specifying file extensions for `gr.File` and `gr.UploadButton`, using `file_types` parameter (e.g `gr.File(file_count="multiple", file_types=["text", ".json", ".csv"])`) by @dawoodkhan82 in [#2901](https://github.com/gradio-app/gradio/pull/2901)
- Added `multiselect` option to `Dropdown` by @dawoodkhan82 in [#2871](https://github.com/gradio-app/gradio/pull/2871)

### With `multiselect` set to `true` a user can now select multiple options from the `gr.Dropdown` component.

```python
gr.Dropdown(["angola", "pakistan", "canada"], multiselect=True, value=["angola"])
```

<img width="610" alt="Screenshot 2023-01-03 at 4 14 36 PM" src="https://user-images.githubusercontent.com/12725292/210442547-c86975c9-4b4f-4b8e-8803-9d96e6a8583a.png">

## Bug Fixes:

- Fixed bug where an error opening an audio file led to a crash by [@FelixDombek](https://github.com/FelixDombek) in [PR 2898](https://github.com/gradio-app/gradio/pull/2898)
- Fixed bug where setting `default_enabled=False` made it so that the entire queue did not start by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2876](https://github.com/gradio-app/gradio/pull/2876)
- Fixed bug where csv preview for DataFrame examples would show filename instead of file contents by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2877](https://github.com/gradio-app/gradio/pull/2877)
- Fixed bug where an error raised after yielding iterative output would not be displayed in the browser by
  [@JaySmithWpg](https://github.com/JaySmithWpg) in [PR 2889](https://github.com/gradio-app/gradio/pull/2889)
- Fixed bug in `blocks_style` demo that was preventing it from launching by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2890](https://github.com/gradio-app/gradio/pull/2890)
- Fixed bug where files could not be downloaded by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2926](https://github.com/gradio-app/gradio/pull/2926)
- Fixed bug where cached examples were not displaying properly by [@a-rogalska](https://github.com/a-rogalska) in [PR 2974](https://github.com/gradio-app/gradio/pull/2974)

## Documentation Changes:

- Added a Guide on using Google Sheets to create a real-time dashboard with Gradio's `DataFrame` and `LinePlot` component, by [@abidlabs](https://github.com/abidlabs) in [PR 2816](https://github.com/gradio-app/gradio/pull/2816)
- Add a components - events matrix on the docs by [@aliabd](https://github.com/aliabd) in [PR 2921](https://github.com/gradio-app/gradio/pull/2921)

## Testing and Infrastructure Changes:

- Deployed PRs from forks to spaces by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2895](https://github.com/gradio-app/gradio/pull/2895)

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- The `default_enabled` parameter of the `Blocks.queue` method has no effect by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2876](https://github.com/gradio-app/gradio/pull/2876)
- Added typing to several Python files in codebase by [@abidlabs](https://github.com/abidlabs) in [PR 2887](https://github.com/gradio-app/gradio/pull/2887)
- Excluding untracked files from demo notebook check action by [@aliabd](https://github.com/aliabd) in [PR 2897](https://github.com/gradio-app/gradio/pull/2897)
- Optimize images and gifs by [@aliabd](https://github.com/aliabd) in [PR 2922](https://github.com/gradio-app/gradio/pull/2922)
- Updated typing by [@1nF0rmed](https://github.com/1nF0rmed) in [PR 2904](https://github.com/gradio-app/gradio/pull/2904)

## Contributors Shoutout:

- @JaySmithWpg for making their first contribution to gradio!
- @MohamedAliRashad for making their first contribution to gradio!

# Version 3.15.0

## New Features:

Gradio's newest plotting component `gr.LinePlot`! 📈

With this component you can easily create time series visualizations with customizable
appearance for your demos and dashboards ... all without having to know an external plotting library.

For an example of the api see below:

```python
gr.LinePlot(stocks,
            x="date",
            y="price",
            color="symbol",
            color_legend_position="bottom",
            width=600, height=400, title="Stock Prices")
```

![image](https://user-images.githubusercontent.com/41651716/208711646-81ae3745-149b-46a3-babd-0569aecdd409.png)

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2807](https://github.com/gradio-app/gradio/pull/2807)

## Bug Fixes:

- Fixed bug where the `examples_per_page` parameter of the `Examples` component was not passed to the internal `Dataset` component by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2861](https://github.com/gradio-app/gradio/pull/2861)
- Fixes loading Spaces that have components with default values by [@abidlabs](https://github.com/abidlabs) in [PR 2855](https://github.com/gradio-app/gradio/pull/2855)
- Fixes flagging when `allow_flagging="auto"` in `gr.Interface()` by [@abidlabs](https://github.com/abidlabs) in [PR 2695](https://github.com/gradio-app/gradio/pull/2695)
- Fixed bug where passing a non-list value to `gr.CheckboxGroup` would crash the entire app by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2866](https://github.com/gradio-app/gradio/pull/2866)

## Documentation Changes:

- Added a Guide on using BigQuery with Gradio's `DataFrame` and `ScatterPlot` component,
  by [@abidlabs](https://github.com/abidlabs) in [PR 2794](https://github.com/gradio-app/gradio/pull/2794)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Fixed importing gradio can cause PIL.Image.registered_extensions() to break by `[@aliencaocao](https://github.com/aliencaocao)` in `[PR 2846](https://github.com/gradio-app/gradio/pull/2846)`
- Fix css glitch and navigation in docs by [@aliabd](https://github.com/aliabd) in [PR 2856](https://github.com/gradio-app/gradio/pull/2856)
- Added the ability to set `x_lim`, `y_lim` and legend positions for `gr.ScatterPlot` by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2807](https://github.com/gradio-app/gradio/pull/2807)
- Remove footers and min-height the correct way by [@aliabd](https://github.com/aliabd) in [PR 2860](https://github.com/gradio-app/gradio/pull/2860)

## Contributors Shoutout:

No changes to highlight.

# Version 3.14.0

## New Features:

### Add Waveform Visual Support to Audio

Adds a `gr.make_waveform()` function that creates a waveform video by combining an audio and an optional background image by [@dawoodkhan82](http://github.com/dawoodkhan82) and [@aliabid94](http://github.com/aliabid94) in [PR 2706](https://github.com/gradio-app/gradio/pull/2706. Helpful for making audio outputs much more shareable.

![waveform screenrecording](https://user-images.githubusercontent.com/7870876/206062396-164a5e71-451a-4fe0-94a7-cbe9269d57e6.gif)

### Allows Every Component to Accept an `every` Parameter

When a component's initial value is a function, the `every` parameter re-runs the function every `every` seconds. By [@abidlabs](https://github.com/abidlabs) in [PR 2806](https://github.com/gradio-app/gradio/pull/2806). Here's a code example:

```py
import gradio as gr

with gr.Blocks() as demo:
    df = gr.DataFrame(run_query, every=60*60)

demo.queue().launch()
```

## Bug Fixes:

- Fixed issue where too many temporary files were created, all with randomly generated
  filepaths. Now fewer temporary files are created and are assigned a path that is a
  hash based on the file contents by [@abidlabs](https://github.com/abidlabs) in [PR 2758](https://github.com/gradio-app/gradio/pull/2758)

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.13.2

## New Features:

No changes to highlight.

## Bug Fixes:

\*No changes to highlight.

-

## Documentation Changes:

- Improves documentation of several queuing-related parameters by [@abidlabs](https://github.com/abidlabs) in [PR 2825](https://github.com/gradio-app/gradio/pull/2825)

## Testing and Infrastructure Changes:

- Remove h11 pinning by [@ecederstrand](https://github.com/ecederstrand) in [PR 2820](https://github.com/gradio-app/gradio/pull/2820)

## Breaking Changes:

No changes to highlight.

## Full Changelog:

No changes to highlight.

## Contributors Shoutout:

No changes to highlight.

# Version 3.13.1

## New Features:

### New Shareable Links

Replaces tunneling logic based on ssh port-forwarding to that based on `frp` by [XciD](https://github.com/XciD) and [Wauplin](https://github.com/Wauplin) in [PR 2509](https://github.com/gradio-app/gradio/pull/2509)

You don't need to do anything differently, but when you set `share=True` in `launch()`,
you'll get this message and a public link that look a little bit different:

```bash
Setting up a public link... we have recently upgraded the way public links are generated. If you encounter any problems, please downgrade to gradio version 3.13.0
.
Running on public URL: https://bec81a83-5b5c-471e.gradio.live
```

These links are a more secure and scalable way to create shareable demos!

## Bug Fixes:

- Allows `gr.Dataframe()` to take a `pandas.DataFrame` that includes numpy array and other types as its initial value, by [@abidlabs](https://github.com/abidlabs) in [PR 2804](https://github.com/gradio-app/gradio/pull/2804)
- Add `altair` to requirements.txt by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2811](https://github.com/gradio-app/gradio/pull/2811)
- Added aria-labels to icon buttons that are built into UI components by [@emilyuhde](http://github.com/emilyuhde) in [PR 2791](https://github.com/gradio-app/gradio/pull/2791)

## Documentation Changes:

- Fixed some typos in the "Plot Component for Maps" guide by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2811](https://github.com/gradio-app/gradio/pull/2811)

## Testing and Infrastructure Changes:

- Fixed test for IP address by [@abidlabs](https://github.com/abidlabs) in [PR 2808](https://github.com/gradio-app/gradio/pull/2808)

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Fixed typo in parameter `visible` in classes in `templates.py` by [@abidlabs](https://github.com/abidlabs) in [PR 2805](https://github.com/gradio-app/gradio/pull/2805)
- Switched external service for getting IP address from `https://api.ipify.org` to `https://checkip.amazonaws.com/` by [@abidlabs](https://github.com/abidlabs) in [PR 2810](https://github.com/gradio-app/gradio/pull/2810)

## Contributors Shoutout:

No changes to highlight.

- Fixed typo in parameter `visible` in classes in `templates.py` by [@abidlabs](https://github.com/abidlabs) in [PR 2805](https://github.com/gradio-app/gradio/pull/2805)
- Switched external service for getting IP address from `https://api.ipify.org` to `https://checkip.amazonaws.com/` by [@abidlabs](https://github.com/abidlabs) in [PR 2810](https://github.com/gradio-app/gradio/pull/2810)

# Version 3.13.0

## New Features:

### Scatter plot component

It is now possible to create a scatter plot natively in Gradio!

The `gr.ScatterPlot` component accepts a pandas dataframe and some optional configuration parameters
and will automatically create a plot for you!

This is the first of many native plotting components in Gradio!

For an example of how to use `gr.ScatterPlot` see below:

```python
import gradio as gr
from vega_datasets import data

cars = data.cars()

with gr.Blocks() as demo:
    gr.ScatterPlot(show_label=False,
                   value=cars,
                   x="Horsepower",
                   y="Miles_per_Gallon",
                   color="Origin",
                   tooltip="Name",
                   title="Car Data",
                   y_title="Miles per Gallon",
                   color_legend_title="Origin of Car").style(container=False)

demo.launch()
```

<img width="404" alt="image" src="https://user-images.githubusercontent.com/41651716/206737726-4c4da5f0-dee8-4f0a-b1e1-e2b75c4638e9.png">

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2764](https://github.com/gradio-app/gradio/pull/2764)

### Support for altair plots

The `Plot` component can now accept altair plots as values!
Simply return an altair plot from your event listener and gradio will display it in the front-end.
See the example below:

```python
import gradio as gr
import altair as alt
from vega_datasets import data

cars = data.cars()
chart = (
    alt.Chart(cars)
    .mark_point()
    .encode(
        x="Horsepower",
        y="Miles_per_Gallon",
        color="Origin",
    )
)

with gr.Blocks() as demo:
    gr.Plot(value=chart)
demo.launch()
```

<img width="1366" alt="image" src="https://user-images.githubusercontent.com/41651716/204660697-f994316f-5ca7-4e8a-93bc-eb5e0d556c91.png">

By [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2741](https://github.com/gradio-app/gradio/pull/2741)

### Set the background color of a Label component

The `Label` component now accepts a `color` argument by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2736](https://github.com/gradio-app/gradio/pull/2736).
The `color` argument should either be a valid css color name or hexadecimal string.
You can update the color with `gr.Label.update`!

This lets you create Alert and Warning boxes with the `Label` component. See below:

```python
import gradio as gr
import random

def update_color(value):
    if value < 0:
        # This is bad so use red
        return "#FF0000"
    elif 0 <= value <= 20:
        # Ok but pay attention (use orange)
        return "#ff9966"
    else:
        # Nothing to worry about
        return None

def update_value():
    choice = random.choice(['good', 'bad', 'so-so'])
    color = update_color(choice)
    return gr.Label.update(value=choice, color=color)


with gr.Blocks() as demo:
    label = gr.Label(value=-10)
    demo.load(lambda: update_value(), inputs=None, outputs=[label], every=1)
demo.queue().launch()
```

![label_bg_color_update](https://user-images.githubusercontent.com/41651716/204400372-80e53857-f26f-4a38-a1ae-1acadff75e89.gif)

### Add Brazilian Portuguese translation

Add Brazilian Portuguese translation (pt-BR.json) by [@pstwh](http://github.com/pstwh) in [PR 2753](https://github.com/gradio-app/gradio/pull/2753):

<img width="951" alt="image" src="https://user-images.githubusercontent.com/1778297/206615305-4c52031e-3f7d-4df2-8805-a79894206911.png">

## Bug Fixes:

- Fixed issue where image thumbnails were not showing when an example directory was provided
  by [@abidlabs](https://github.com/abidlabs) in [PR 2745](https://github.com/gradio-app/gradio/pull/2745)
- Fixed bug loading audio input models from the hub by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2779](https://github.com/gradio-app/gradio/pull/2779).
- Fixed issue where entities were not merged when highlighted text was generated from the
  dictionary inputs [@payoto](https://github.com/payoto) in [PR 2767](https://github.com/gradio-app/gradio/pull/2767)
- Fixed bug where generating events did not finish running even if the websocket connection was closed by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2783](https://github.com/gradio-app/gradio/pull/2783).

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Images in the chatbot component are now resized if they exceed a max width by [@abidlabs](https://github.com/abidlabs) in [PR 2748](https://github.com/gradio-app/gradio/pull/2748)
- Missing parameters have been added to `gr.Blocks().load()` by [@abidlabs](https://github.com/abidlabs) in [PR 2755](https://github.com/gradio-app/gradio/pull/2755)
- Deindex share URLs from search by [@aliabd](https://github.com/aliabd) in [PR 2772](https://github.com/gradio-app/gradio/pull/2772)
- Redirect old links and fix broken ones by [@aliabd](https://github.com/aliabd) in [PR 2774](https://github.com/gradio-app/gradio/pull/2774)

## Contributors Shoutout:

No changes to highlight.

# Version 3.12.0

## New Features:

### The `Chatbot` component now supports a subset of Markdown (including bold, italics, code, images)

You can now pass in some Markdown to the Chatbot component and it will show up,
meaning that you can pass in images as well! by [@abidlabs](https://github.com/abidlabs) in [PR 2731](https://github.com/gradio-app/gradio/pull/2731)

Here's a simple example that references a local image `lion.jpg` that is in the same
folder as the Python script:

```py
import gradio as gr

with gr.Blocks() as demo:
    gr.Chatbot([("hi", "hello **abubakar**"), ("![](/file=lion.jpg)", "cool pic")])

demo.launch()
```

![Alt text](https://user-images.githubusercontent.com/1778297/204357455-5c1a4002-eee7-479d-9a1e-ba2c12522723.png)

To see a more realistic example, see the new demo `/demo/chatbot_multimodal/run.py`.

### Latex support

Added mathtext (a subset of latex) support to gr.Markdown. Added by [@kashif](https://github.com/kashif) and [@aliabid94](https://github.com/aliabid94) in [PR 2696](https://github.com/gradio-app/gradio/pull/2696).

Example of how it can be used:

```python
gr.Markdown(
    r"""
    # Hello World! $\frac{\sqrt{x + y}}{4}$ is today's lesson.
    """)
```

### Update Accordion properties from the backend

You can now update the Accordion `label` and `open` status with `gr.Accordion.update` by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2690](https://github.com/gradio-app/gradio/pull/2690)

```python
import gradio as gr

with gr.Blocks() as demo:
    with gr.Accordion(label="Open for greeting", open=False) as accordion:
        gr.Textbox("Hello!")
    open_btn = gr.Button(value="Open Accordion")
    close_btn = gr.Button(value="Close Accordion")
    open_btn.click(
        lambda: gr.Accordion.update(open=True, label="Open Accordion"),
        inputs=None,
        outputs=[accordion],
    )
    close_btn.click(
        lambda: gr.Accordion.update(open=False, label="Closed Accordion"),
        inputs=None,
        outputs=[accordion],
    )
demo.launch()
```

![update_accordion](https://user-images.githubusercontent.com/41651716/203164176-b102eae3-babe-4986-ae30-3ab4f400cedc.gif)

## Bug Fixes:

- Fixed bug where requests timeout is missing from utils.version_check() by [@yujiehecs](https://github.com/yujiehecs) in [PR 2729](https://github.com/gradio-app/gradio/pull/2729)
- Fixed bug where so that the `File` component can properly preprocess files to "binary" byte-string format by [CoffeeVampir3](https://github.com/CoffeeVampir3) in [PR 2727](https://github.com/gradio-app/gradio/pull/2727)
- Fixed bug to ensure that filenames are less than 200 characters even for non-English languages by [@SkyTNT](https://github.com/SkyTNT) in [PR 2685](https://github.com/gradio-app/gradio/pull/2685)

## Documentation Changes:

- Performance improvements to docs on mobile by [@aliabd](https://github.com/aliabd) in [PR 2730](https://github.com/gradio-app/gradio/pull/2730)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Make try examples button more prominent by [@aliabd](https://github.com/aliabd) in [PR 2705](https://github.com/gradio-app/gradio/pull/2705)
- Fix id clashes in docs by [@aliabd](https://github.com/aliabd) in [PR 2713](https://github.com/gradio-app/gradio/pull/2713)
- Fix typos in guide docs by [@andridns](https://github.com/andridns) in [PR 2722](https://github.com/gradio-app/gradio/pull/2722)
- Add option to `include_audio` in Video component. When `True`, for `source="webcam"` this will record audio and video, for `source="upload"` this will retain the audio in an uploaded video by [@mandargogate](https://github.com/MandarGogate) in [PR 2721](https://github.com/gradio-app/gradio/pull/2721)

## Contributors Shoutout:

- [@andridns](https://github.com/andridns) made their first contribution in [PR 2722](https://github.com/gradio-app/gradio/pull/2722)!

# Version 3.11.0

## New Features:

### Upload Button

There is now a new component called the `UploadButton` which is a file upload component but in button form! You can also specify what file types it should accept in the form of a list (ex: `image`, `video`, `audio`, `text`, or generic `file`). Added by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2591](https://github.com/gradio-app/gradio/pull/2591).

Example of how it can be used:

```python
import gradio as gr

def upload_file(files):
    file_paths = [file.name for file in files]
    return file_paths

with gr.Blocks() as demo:
    file_output = gr.File()
    upload_button = gr.UploadButton("Click to Upload a File", file_types=["image", "video"], file_count="multiple")
    upload_button.upload(upload_file, upload_button, file_output)

demo.launch()
```

### Revamped API documentation page

New API Docs page with in-browser playground and updated aesthetics. [@gary149](https://github.com/gary149) in [PR 2652](https://github.com/gradio-app/gradio/pull/2652)

### Revamped Login page

Previously our login page had its own CSS, had no dark mode, and had an ugly json message on the wrong credentials. Made the page more aesthetically consistent, added dark mode support, and a nicer error message. [@aliabid94](https://github.com/aliabid94) in [PR 2684](https://github.com/gradio-app/gradio/pull/2684)

### Accessing the Requests Object Directly

You can now access the Request object directly in your Python function by [@abidlabs](https://github.com/abidlabs) in [PR 2641](https://github.com/gradio-app/gradio/pull/2641). This means that you can access request headers, the client IP address, and so on. In order to use it, add a parameter to your function and set its type hint to be `gr.Request`. Here's a simple example:

```py
import gradio as gr

def echo(name, request: gr.Request):
    if request:
        print("Request headers dictionary:", request.headers)
        print("IP address:", request.client.host)
    return name

io = gr.Interface(echo, "textbox", "textbox").launch()
```

## Bug Fixes:

- Fixed bug that limited files from being sent over websockets to 16MB. The new limit
  is now 1GB by [@abidlabs](https://github.com/abidlabs) in [PR 2709](https://github.com/gradio-app/gradio/pull/2709)

## Documentation Changes:

- Updated documentation for embedding Gradio demos on Spaces as web components by
  [@julien-c](https://github.com/julien-c) in [PR 2698](https://github.com/gradio-app/gradio/pull/2698)
- Updated IFrames in Guides to use the host URL instead of the Space name to be consistent with the new method for embedding Spaces, by
  [@julien-c](https://github.com/julien-c) in [PR 2692](https://github.com/gradio-app/gradio/pull/2692)
- Colab buttons on every demo in the website! Just click open in colab, and run the demo there.

https://user-images.githubusercontent.com/9021060/202878400-cb16ed47-f4dd-4cb0-b2f0-102a9ff64135.mov

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Better warnings and error messages for `gr.Interface.load()` by [@abidlabs](https://github.com/abidlabs) in [PR 2694](https://github.com/gradio-app/gradio/pull/2694)
- Add open in colab buttons to demos in docs and /demos by [@aliabd](https://github.com/aliabd) in [PR 2608](https://github.com/gradio-app/gradio/pull/2608)
- Apply different formatting for the types in component docstrings by [@aliabd](https://github.com/aliabd) in [PR 2707](https://github.com/gradio-app/gradio/pull/2707)

## Contributors Shoutout:

No changes to highlight.

# Version 3.10.1

## New Features:

No changes to highlight.

## Bug Fixes:

- Passes kwargs into `gr.Interface.load()` by [@abidlabs](https://github.com/abidlabs) in [PR 2669](https://github.com/gradio-app/gradio/pull/2669)

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Clean up printed statements in Embedded Colab Mode by [@aliabid94](https://github.com/aliabid94) in [PR 2612](https://github.com/gradio-app/gradio/pull/2612)

## Contributors Shoutout:

No changes to highlight.

# Version 3.10.0

- Add support for `'password'` and `'email'` types to `Textbox`. [@pngwn](https://github.com/pngwn) in [PR 2653](https://github.com/gradio-app/gradio/pull/2653)
- `gr.Textbox` component will now raise an exception if `type` is not "text", "email", or "password" [@pngwn](https://github.com/pngwn) in [PR 2653](https://github.com/gradio-app/gradio/pull/2653). This will cause demos using the deprecated `gr.Textbox(type="number")` to raise an exception.

## Bug Fixes:

- Updated the minimum FastApi used in tests to version 0.87 by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2647](https://github.com/gradio-app/gradio/pull/2647)
- Fixed bug where interfaces with examples could not be loaded with `gr.Interface.load` by [@freddyaboulton](https://github.com/freddyaboulton) [PR 2640](https://github.com/gradio-app/gradio/pull/2640)
- Fixed bug where the `interactive` property of a component could not be updated by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2639](https://github.com/gradio-app/gradio/pull/2639)
- Fixed bug where some URLs were not being recognized as valid URLs and thus were not
  loading correctly in various components by [@abidlabs](https://github.com/abidlabs) in [PR 2659](https://github.com/gradio-app/gradio/pull/2659)

## Documentation Changes:

- Fix some typos in the embedded demo names in "05_using_blocks_like_functions.md" by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2656](https://github.com/gradio-app/gradio/pull/2656)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Add support for `'password'` and `'email'` types to `Textbox`. [@pngwn](https://github.com/pngwn) in [PR 2653](https://github.com/gradio-app/gradio/pull/2653)

## Contributors Shoutout:

No changes to highlight.

# Version 3.9.1

## New Features:

No changes to highlight.

## Bug Fixes:

- Only set a min height on md and html when loading by [@pngwn](https://github.com/pngwn) in [PR 2623](https://github.com/gradio-app/gradio/pull/2623)

## Documentation Changes:

- See docs for the latest gradio commit to main as well the latest pip release:

![main-vs-pip](https://user-images.githubusercontent.com/9021060/199607887-aab1ae4e-a070-4527-966d-024397abe15b.gif)

- Modified the "Connecting To a Database Guide" to use `pd.read_sql` as opposed to low-level postgres connector by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2604](https://github.com/gradio-app/gradio/pull/2604)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Dropdown for seeing docs as latest or main by [@aliabd](https://github.com/aliabd) in [PR 2544](https://github.com/gradio-app/gradio/pull/2544)
- Allow `gr.Templates` to accept parameters to override the defaults by [@abidlabs](https://github.com/abidlabs) in [PR 2600](https://github.com/gradio-app/gradio/pull/2600)
- Components now throw a `ValueError()` if constructed with invalid parameters for `type` or `source` (for components that take those parameters) in [PR 2610](https://github.com/gradio-app/gradio/pull/2610)
- Allow auth with using queue by [@GLGDLY](https://github.com/GLGDLY) in [PR 2611](https://github.com/gradio-app/gradio/pull/2611)

## Contributors Shoutout:

No changes to highlight.

# Version 3.9

## New Features:

- Gradio is now embedded directly in colab without requiring the share link by [@aliabid94](https://github.com/aliabid94) in [PR 2455](https://github.com/gradio-app/gradio/pull/2455)

### Calling functions by api_name in loaded apps

When you load an upstream app with `gr.Blocks.load`, you can now specify which fn
to call with the `api_name` parameter.

```python
import gradio as gr
english_translator = gr.Blocks.load(name="spaces/gradio/english-translator")
german = english_translator("My name is Freddy", api_name='translate-to-german')
```

The `api_name` parameter will take precedence over the `fn_index` parameter.

## Bug Fixes:

- Fixed bug where None could not be used for File,Model3D, and Audio examples by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2588](https://github.com/gradio-app/gradio/pull/2588)
- Fixed links in Plotly map guide + demo by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2578](https://github.com/gradio-app/gradio/pull/2578)
- `gr.Blocks.load()` now correctly loads example files from Spaces [@abidlabs](https://github.com/abidlabs) in [PR 2594](https://github.com/gradio-app/gradio/pull/2594)
- Fixed bug when image clear started upload dialog [@mezotaken](https://github.com/mezotaken) in [PR 2577](https://github.com/gradio-app/gradio/pull/2577)

## Documentation Changes:

- Added a Guide on how to configure the queue for maximum performance by [@abidlabs](https://github.com/abidlabs) in [PR 2558](https://github.com/gradio-app/gradio/pull/2558)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Add `api_name` to `Blocks.__call__` by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2593](https://github.com/gradio-app/gradio/pull/2593)
- Update queue with using deque & update requirements by [@GLGDLY](https://github.com/GLGDLY) in [PR 2428](https://github.com/gradio-app/gradio/pull/2428)

## Contributors Shoutout:

No changes to highlight.

# Version 3.8.2

## Bug Fixes:

- Ensure gradio apps embedded via spaces use the correct endpoint for predictions. [@pngwn](https://github.com/pngwn) in [PR 2567](https://github.com/gradio-app/gradio/pull/2567)
- Ensure gradio apps embedded via spaces use the correct websocket protocol. [@pngwn](https://github.com/pngwn) in [PR 2571](https://github.com/gradio-app/gradio/pull/2571)

## New Features:

### Running Events Continuously

Gradio now supports the ability to run an event continuously on a fixed schedule. To use this feature,
pass `every=# of seconds` to the event definition. This will run the event every given number of seconds!

This can be used to:

- Create live visualizations that show the most up to date data
- Refresh the state of the frontend automatically in response to changes in the backend

Here is an example of a live plot that refreshes every half second:

```python
import math
import gradio as gr
import plotly.express as px
import numpy as np


plot_end = 2 * math.pi


def get_plot(period=1):
    global plot_end
    x = np.arange(plot_end - 2 * math.pi, plot_end, 0.02)
    y = np.sin(2*math.pi*period * x)
    fig = px.line(x=x, y=y)
    plot_end += 2 * math.pi
    return fig


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown("Change the value of the slider to automatically update the plot")
            period = gr.Slider(label="Period of plot", value=1, minimum=0, maximum=10, step=1)
            plot = gr.Plot(label="Plot (updates every half second)")

    dep = demo.load(get_plot, None, plot, every=0.5)
    period.change(get_plot, period, plot, every=0.5, cancels=[dep])

demo.queue().launch()
```

![live_demo](https://user-images.githubusercontent.com/41651716/198357377-633ce460-4e31-47bd-8202-1440cdd6fe19.gif)

## Bug Fixes:

No changes to highlight.

## Documentation Changes:

- Explained how to set up `queue` and `auth` when working with reload mode by by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 3089](https://github.com/gradio-app/gradio/pull/3089)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Allows loading private Spaces by passing an an `api_key` to `gr.Interface.load()`
  by [@abidlabs](https://github.com/abidlabs) in [PR 2568](https://github.com/gradio-app/gradio/pull/2568)

## Contributors Shoutout:

No changes to highlight.

# Version 3.8

## New Features:

- Allows event listeners to accept a single dictionary as its argument, where the keys are the components and the values are the component values. This is set by passing the input components in the event listener as a set instead of a list. [@aliabid94](https://github.com/aliabid94) in [PR 2550](https://github.com/gradio-app/gradio/pull/2550)

## Bug Fixes:

- Fix whitespace issue when using plotly. [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2548](https://github.com/gradio-app/gradio/pull/2548)
- Apply appropriate alt text to all gallery images. [@camenduru](https://github.com/camenduru) in [PR 2358](https://github.com/gradio-app/gradio/pull/2538)
- Removed erroneous tkinter import in gradio.blocks by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2555](https://github.com/gradio-app/gradio/pull/2555)

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Added the `every` keyword to event listeners that runs events on a fixed schedule by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2512](https://github.com/gradio-app/gradio/pull/2512)
- Fix whitespace issue when using plotly. [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2548](https://github.com/gradio-app/gradio/pull/2548)
- Apply appropriate alt text to all gallery images. [@camenduru](https://github.com/camenduru) in [PR 2358](https://github.com/gradio-app/gradio/pull/2538)

## Contributors Shoutout:

No changes to highlight.

# Version 3.7

## New Features:

### Batched Functions

Gradio now supports the ability to pass _batched_ functions. Batched functions are just
functions which take in a list of inputs and return a list of predictions.

For example, here is a batched function that takes in two lists of inputs (a list of
words and a list of ints), and returns a list of trimmed words as output:

```py
import time

def trim_words(words, lens):
    trimmed_words = []
    time.sleep(5)
    for w, l in zip(words, lens):
        trimmed_words.append(w[:l])
    return [trimmed_words]
```

The advantage of using batched functions is that if you enable queuing, the Gradio
server can automatically _batch_ incoming requests and process them in parallel,
potentially speeding up your demo. Here's what the Gradio code looks like (notice
the `batch=True` and `max_batch_size=16` -- both of these parameters can be passed
into event triggers or into the `Interface` class)

```py
import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        word = gr.Textbox(label="word", value="abc")
        leng = gr.Number(label="leng", precision=0, value=1)
        output = gr.Textbox(label="Output")
    with gr.Row():
        run = gr.Button()

    event = run.click(trim_words, [word, leng], output, batch=True, max_batch_size=16)

demo.queue()
demo.launch()
```

In the example above, 16 requests could be processed in parallel (for a total inference
time of 5 seconds), instead of each request being processed separately (for a total
inference time of 80 seconds).

### Upload Event

`Video`, `Audio`, `Image`, and `File` components now support a `upload()` event that is triggered when a user uploads a file into any of these components.

Example usage:

```py
import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        input_video = gr.Video()
        output_video = gr.Video()

     # Clears the output video when an input video is uploaded
    input_video.upload(lambda : None, None, output_video)
```

## Bug Fixes:

- Fixes issue where plotly animations, interactivity, titles, legends, were not working properly. [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2486](https://github.com/gradio-app/gradio/pull/2486)
- Prevent requests to the `/api` endpoint from skipping the queue if the queue is enabled for that event by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2493](https://github.com/gradio-app/gradio/pull/2493)
- Fixes a bug with `cancels` in event triggers so that it works properly if multiple
  Blocks are rendered by [@abidlabs](https://github.com/abidlabs) in [PR 2530](https://github.com/gradio-app/gradio/pull/2530)
- Prevent invalid targets of events from crashing the whole application. [@pngwn](https://github.com/pngwn) in [PR 2534](https://github.com/gradio-app/gradio/pull/2534)
- Properly dequeue cancelled events when multiple apps are rendered by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2540](https://github.com/gradio-app/gradio/pull/2540)

## Documentation Changes:

- Added an example interactive dashboard to the "Tabular & Plots" section of the Demos page by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2508](https://github.com/gradio-app/gradio/pull/2508)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Fixes the error message if a user builds Gradio locally and tries to use `share=True` by [@abidlabs](https://github.com/abidlabs) in [PR 2502](https://github.com/gradio-app/gradio/pull/2502)
- Allows the render() function to return self by [@Raul9595](https://github.com/Raul9595) in [PR 2514](https://github.com/gradio-app/gradio/pull/2514)
- Fixes issue where plotly animations, interactivity, titles, legends, were not working properly. [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2486](https://github.com/gradio-app/gradio/pull/2486)
- Gradio now supports batched functions by [@abidlabs](https://github.com/abidlabs) in [PR 2218](https://github.com/gradio-app/gradio/pull/2218)
- Add `upload` event for `Video`, `Audio`, `Image`, and `File` components [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2448](https://github.com/gradio-app/gradio/pull/2456)
- Changes websocket path for Spaces as it is no longer necessary to have a different URL for websocket connections on Spaces by [@abidlabs](https://github.com/abidlabs) in [PR 2528](https://github.com/gradio-app/gradio/pull/2528)
- Clearer error message when events are defined outside of a Blocks scope, and a warning if you
  try to use `Series` or `Parallel` with `Blocks` by [@abidlabs](https://github.com/abidlabs) in [PR 2543](https://github.com/gradio-app/gradio/pull/2543)
- Adds support for audio samples that are in `float64`, `float16`, or `uint16` formats by [@abidlabs](https://github.com/abidlabs) in [PR 2545](https://github.com/gradio-app/gradio/pull/2545)

## Contributors Shoutout:

No changes to highlight.

# Version 3.6

## New Features:

### Cancelling Running Events

Running events can be cancelled when other events are triggered! To test this feature, pass the `cancels` parameter to the event listener.
For this feature to work, the queue must be enabled.

![cancel_on_change_rl](https://user-images.githubusercontent.com/41651716/195952623-61a606bd-e82b-4e1a-802e-223154cb8727.gif)

Code:

```python
import time
import gradio as gr

def fake_diffusion(steps):
    for i in range(steps):
        time.sleep(1)
        yield str(i)

def long_prediction(*args, **kwargs):
    time.sleep(10)
    return 42


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            n = gr.Slider(1, 10, value=9, step=1, label="Number Steps")
            run = gr.Button()
            output = gr.Textbox(label="Iterative Output")
            stop = gr.Button(value="Stop Iterating")
        with gr.Column():
            prediction = gr.Number(label="Expensive Calculation")
            run_pred = gr.Button(value="Run Expensive Calculation")
        with gr.Column():
            cancel_on_change = gr.Textbox(label="Cancel Iteration and Expensive Calculation on Change")

    click_event = run.click(fake_diffusion, n, output)
    stop.click(fn=None, inputs=None, outputs=None, cancels=[click_event])
    pred_event = run_pred.click(fn=long_prediction, inputs=None, outputs=prediction)

    cancel_on_change.change(None, None, None, cancels=[click_event, pred_event])


demo.queue(concurrency_count=1, max_size=20).launch()
```

For interfaces, a stop button will be added automatically if the function uses a `yield` statement.

```python
import gradio as gr
import time

def iteration(steps):
    for i in range(steps):
       time.sleep(0.5)
       yield i

gr.Interface(iteration,
             inputs=gr.Slider(minimum=1, maximum=10, step=1, value=5),
             outputs=gr.Number()).queue().launch()
```

![stop_interface_rl](https://user-images.githubusercontent.com/41651716/195952883-e7ca4235-aae3-4852-8f28-96d01d0c5822.gif)

## Bug Fixes:

- Add loading status tracker UI to HTML and Markdown components. [@pngwn](https://github.com/pngwn) in [PR 2474](https://github.com/gradio-app/gradio/pull/2474)
- Fixed videos being mirrored in the front-end if source is not webcam by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2475](https://github.com/gradio-app/gradio/pull/2475)
- Add clear button for timeseries component [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2487](https://github.com/gradio-app/gradio/pull/2487)
- Removes special characters from temporary filenames so that the files can be served by components [@abidlabs](https://github.com/abidlabs) in [PR 2480](https://github.com/gradio-app/gradio/pull/2480)
- Fixed infinite reload loop when mounting gradio as a sub application by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2477](https://github.com/gradio-app/gradio/pull/2477)

## Documentation Changes:

- Adds a demo to show how a sound alert can be played upon completion of a prediction by [@abidlabs](https://github.com/abidlabs) in [PR 2478](https://github.com/gradio-app/gradio/pull/2478)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Enable running events to be cancelled from other events by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2433](https://github.com/gradio-app/gradio/pull/2433)
- Small fix for version check before reuploading demos by [@aliabd](https://github.com/aliabd) in [PR 2469](https://github.com/gradio-app/gradio/pull/2469)
- Add loading status tracker UI to HTML and Markdown components. [@pngwn](https://github.com/pngwn) in [PR 2400](https://github.com/gradio-app/gradio/pull/2474)
- Add clear button for timeseries component [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2487](https://github.com/gradio-app/gradio/pull/2487)

## Contributors Shoutout:

No changes to highlight.

# Version 3.5

## Bug Fixes:

- Ensure that Gradio does not take control of the HTML page title when embedding a gradio app as a web component, this behaviour flipped by adding `control_page_title="true"` to the webcomponent. [@pngwn](https://github.com/pngwn) in [PR 2400](https://github.com/gradio-app/gradio/pull/2400)
- Decreased latency in iterative-output demos by making the iteration asynchronous [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2409](https://github.com/gradio-app/gradio/pull/2409)
- Fixed queue getting stuck under very high load by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2374](https://github.com/gradio-app/gradio/pull/2374)
- Ensure that components always behave as if `interactive=True` were set when the following conditions are true:

  - no default value is provided,
  - they are not set as the input or output of an event,
  - `interactive` kwarg is not set.

  [@pngwn](https://github.com/pngwn) in [PR 2459](https://github.com/gradio-app/gradio/pull/2459)

## New Features:

- When an `Image` component is set to `source="upload"`, it is now possible to drag and drop and image to replace a previously uploaded image by [@pngwn](https://github.com/pngwn) in [PR 1711](https://github.com/gradio-app/gradio/issues/1711)
- The `gr.Dataset` component now accepts `HTML` and `Markdown` components by [@abidlabs](https://github.com/abidlabs) in [PR 2437](https://github.com/gradio-app/gradio/pull/2437)

## Documentation Changes:

- Improved documentation for the `gr.Dataset` component by [@abidlabs](https://github.com/abidlabs) in [PR 2437](https://github.com/gradio-app/gradio/pull/2437)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

- The `Carousel` component is officially deprecated. Since gradio 3.0, code containing the `Carousel` component would throw warnings. As of the next release, the `Carousel` component will raise an exception.

## Full Changelog:

- Speeds up Gallery component by using temporary files instead of base64 representation in the front-end by [@proxyphi](https://github.com/proxyphi), [@pngwn](https://github.com/pngwn), and [@abidlabs](https://github.com/abidlabs) in [PR 2265](https://github.com/gradio-app/gradio/pull/2265)
- Fixed some embedded demos in the guides by not loading the gradio web component in some guides by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2403](https://github.com/gradio-app/gradio/pull/2403)
- When an `Image` component is set to `source="upload"`, it is now possible to drag and drop and image to replace a previously uploaded image by [@pngwn](https://github.com/pngwn) in [PR 2400](https://github.com/gradio-app/gradio/pull/2410)
- Improve documentation of the `Blocks.load()` event by [@abidlabs](https://github.com/abidlabs) in [PR 2413](https://github.com/gradio-app/gradio/pull/2413)
- Decreased latency in iterative-output demos by making the iteration asynchronous [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2409](https://github.com/gradio-app/gradio/pull/2409)
- Updated share link message to reference new Spaces Hardware [@abidlabs](https://github.com/abidlabs) in [PR 2423](https://github.com/gradio-app/gradio/pull/2423)
- Automatically restart spaces if they're down by [@aliabd](https://github.com/aliabd) in [PR 2405](https://github.com/gradio-app/gradio/pull/2405)
- Carousel component is now deprecated by [@abidlabs](https://github.com/abidlabs) in [PR 2434](https://github.com/gradio-app/gradio/pull/2434)
- Build Gradio from source in ui tests by by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2440](https://github.com/gradio-app/gradio/pull/2440)
- Change "return ValueError" to "raise ValueError" by [@vzakharov](https://github.com/vzakharov) in [PR 2445](https://github.com/gradio-app/gradio/pull/2445)
- Add guide on creating a map demo using the `gr.Plot()` component [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2402](https://github.com/gradio-app/gradio/pull/2402)
- Add blur event for `Textbox` and `Number` components [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2448](https://github.com/gradio-app/gradio/pull/2448)
- Stops a gradio launch from hogging a port even after it's been killed [@aliabid94](https://github.com/aliabid94) in [PR 2453](https://github.com/gradio-app/gradio/pull/2453)
- Fix embedded interfaces on touch screen devices by [@aliabd](https://github.com/aliabd) in [PR 2457](https://github.com/gradio-app/gradio/pull/2457)
- Upload all demos to spaces by [@aliabd](https://github.com/aliabd) in [PR 2281](https://github.com/gradio-app/gradio/pull/2281)

## Contributors Shoutout:

No changes to highlight.

# Version 3.4.1

## New Features:

### 1. See Past and Upcoming Changes in the Release History 👀

You can now see gradio's release history directly on the website, and also keep track of upcoming changes. Just go [here](https://gradio.app/changelog/).

![release-history](https://user-images.githubusercontent.com/9021060/193145458-3de699f7-7620-45de-aa73-a1c1b9b96257.gif)

## Bug Fixes:

1. Fix typo in guide image path by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2357](https://github.com/gradio-app/gradio/pull/2357)
2. Raise error if Blocks has duplicate component with same IDs by [@abidlabs](https://github.com/abidlabs) in [PR 2359](https://github.com/gradio-app/gradio/pull/2359)
3. Catch the permission exception on the audio component by [@Ian-GL](https://github.com/Ian-GL) in [PR 2330](https://github.com/gradio-app/gradio/pull/2330)
4. Fix image_classifier_interface_load demo by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2365](https://github.com/gradio-app/gradio/pull/2365)
5. Fix combining adjacent components without gaps by introducing `gr.Row(variant="compact")` by [@aliabid94](https://github.com/aliabid94) in [PR 2291](https://github.com/gradio-app/gradio/pull/2291) This comes with deprecation of the following arguments for `Component.style`: `round`, `margin`, `border`.
6. Fix audio streaming, which was previously choppy in [PR 2351](https://github.com/gradio-app/gradio/pull/2351). Big thanks to [@yannickfunk](https://github.com/yannickfunk) for the proposed solution.
7. Fix bug where new typeable slider doesn't respect the minimum and maximum values [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2380](https://github.com/gradio-app/gradio/pull/2380)

## Documentation Changes:

1. New Guide: Connecting to a Database 🗄️

   A new guide by [@freddyaboulton](https://github.com/freddyaboulton) that explains how you can use Gradio to connect your app to a database. Read more [here](https://gradio.app/connecting_to_a_database/).

2. New Guide: Running Background Tasks 🥷

   A new guide by [@freddyaboulton](https://github.com/freddyaboulton) that explains how you can run background tasks from your gradio app. Read more [here](https://gradio.app/running_background_tasks/).

3. Small fixes to docs for `Image` component by [@abidlabs](https://github.com/abidlabs) in [PR 2372](https://github.com/gradio-app/gradio/pull/2372)

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- Create a guide on how to connect an app to a database hosted on the cloud by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2341](https://github.com/gradio-app/gradio/pull/2341)
- Removes `analytics` dependency by [@abidlabs](https://github.com/abidlabs) in [PR 2347](https://github.com/gradio-app/gradio/pull/2347)
- Add guide on launching background tasks from your app by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2350](https://github.com/gradio-app/gradio/pull/2350)
- Fix typo in guide image path by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2357](https://github.com/gradio-app/gradio/pull/2357)
- Raise error if Blocks has duplicate component with same IDs by [@abidlabs](https://github.com/abidlabs) in [PR 2359](https://github.com/gradio-app/gradio/pull/2359)
- Hotfix: fix version back to 3.4 by [@abidlabs](https://github.com/abidlabs) in [PR 2361](https://github.com/gradio-app/gradio/pull/2361)
- Change version.txt to 3.4 instead of 3.4.0 by [@aliabd](https://github.com/aliabd) in [PR 2363](https://github.com/gradio-app/gradio/pull/2363)
- Catch the permission exception on the audio component by [@Ian-GL](https://github.com/Ian-GL) in [PR 2330](https://github.com/gradio-app/gradio/pull/2330)
- Fix image_classifier_interface_load demo by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2365](https://github.com/gradio-app/gradio/pull/2365)
- Small fixes to docs for `Image` component by [@abidlabs](https://github.com/abidlabs) in [PR 2372](https://github.com/gradio-app/gradio/pull/2372)
- Automated Release Notes by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2306](https://github.com/gradio-app/gradio/pull/2306)
- Fixed small typos in the docs [@julien-c](https://github.com/julien-c) in [PR 2373](https://github.com/gradio-app/gradio/pull/2373)
- Adds ability to disable pre/post-processing for examples [@abidlabs](https://github.com/abidlabs) in [PR 2383](https://github.com/gradio-app/gradio/pull/2383)
- Copy changelog file in website docker by [@aliabd](https://github.com/aliabd) in [PR 2384](https://github.com/gradio-app/gradio/pull/2384)
- Lets users provide a `gr.update()` dictionary even if post-processing is disabled [@abidlabs](https://github.com/abidlabs) in [PR 2385](https://github.com/gradio-app/gradio/pull/2385)
- Fix bug where errors would cause apps run in reload mode to hang forever by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2394](https://github.com/gradio-app/gradio/pull/2394)
- Fix bug where new typeable slider doesn't respect the minimum and maximum values [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2380](https://github.com/gradio-app/gradio/pull/2380)

## Contributors Shoutout:

No changes to highlight.

# Version 3.4

## New Features:

### 1. Gallery Captions 🖼️

You can now pass captions to images in the Gallery component. To do so you need to pass a {List} of (image, {str} caption) tuples. This is optional and the component also accepts just a list of the images.

Here's an example:

```python
import gradio as gr

images_with_captions = [
    ("https://images.unsplash.com/photo-1551969014-7d2c4cddf0b6", "Cheetah by David Groves"),
    ("https://images.unsplash.com/photo-1546182990-dffeafbe841d", "Lion by Francesco"),
    ("https://images.unsplash.com/photo-1561731216-c3a4d99437d5", "Tiger by Mike Marrah")
    ]

with gr.Blocks() as demo:
    gr.Gallery(value=images_with_captions)

demo.launch()
```

<img src="https://user-images.githubusercontent.com/9021060/192399521-7360b1a9-7ce0-443e-8e94-863a230a7dbe.gif" alt="gallery_captions" width="1000"/>

### 2. Type Values into the Slider 🔢

You can now type values directly on the Slider component! Here's what it looks like:

![type-slider](https://user-images.githubusercontent.com/9021060/192399877-76b662a1-fede-4417-a932-fc15f0da7360.gif)

### 3. Better Sketching and Inpainting 🎨

We've made a lot of changes to our Image component so that it can support better sketching and inpainting.

Now supports:

- A standalone black-and-white sketch

```python
import gradio as gr
demo = gr.Interface(lambda x: x, gr.Sketchpad(), gr.Image())
demo.launch()
```

![bw](https://user-images.githubusercontent.com/9021060/192410264-b08632b5-7b2a-4f86-afb0-5760e7b474cf.gif)

- A standalone color sketch

```python
import gradio as gr
demo = gr.Interface(lambda x: x, gr.Paint(), gr.Image())
demo.launch()
```

![color-sketch](https://user-images.githubusercontent.com/9021060/192410500-3c8c3e64-a5fd-4df2-a991-f0a5cef93728.gif)

- An uploadable image with black-and-white or color sketching

```python
import gradio as gr
demo = gr.Interface(lambda x: x, gr.Image(source='upload', tool='color-sketch'), gr.Image()) # for black and white, tool = 'sketch'
demo.launch()
```

![sketch-new](https://user-images.githubusercontent.com/9021060/192402422-e53cb7b6-024e-448c-87eb-d6a35a63c476.gif)

- Webcam with black-and-white or color sketching

```python
import gradio as gr
demo = gr.Interface(lambda x: x, gr.Image(source='webcam', tool='color-sketch'), gr.Image()) # for black and white, tool = 'sketch'
demo.launch()
```

![webcam-sketch](https://user-images.githubusercontent.com/9021060/192410820-0ffaf324-776e-4e1f-9de6-0fdbbf4940fa.gif)

As well as other fixes

## Bug Fixes:

1. Fix bug where max concurrency count is not respected in queue by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2286](https://github.com/gradio-app/gradio/pull/2286)
2. fix : queue could be blocked by [@SkyTNT](https://github.com/SkyTNT) in [PR 2288](https://github.com/gradio-app/gradio/pull/2288)
3. Supports `gr.update()` in example caching by [@abidlabs](https://github.com/abidlabs) in [PR 2309](https://github.com/gradio-app/gradio/pull/2309)
4. Clipboard fix for iframes by [@abidlabs](https://github.com/abidlabs) in [PR 2321](https://github.com/gradio-app/gradio/pull/2321)
5. Fix: Dataframe column headers are reset when you add a new column by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2318](https://github.com/gradio-app/gradio/pull/2318)
6. Added support for URLs for Video, Audio, and Image by [@abidlabs](https://github.com/abidlabs) in [PR 2256](https://github.com/gradio-app/gradio/pull/2256)
7. Add documentation about how to create and use the Gradio FastAPI app by [@abidlabs](https://github.com/abidlabs) in [PR 2263](https://github.com/gradio-app/gradio/pull/2263)

## Documentation Changes:

1. Adding a Playground Tab to the Website by [@aliabd](https://github.com/aliabd) in [PR 1860](https://github.com/gradio-app/gradio/pull/1860)
2. Gradio for Tabular Data Science Workflows Guide by [@merveenoyan](https://github.com/merveenoyan) in [PR 2199](https://github.com/gradio-app/gradio/pull/2199)
3. Promotes `postprocess` and `preprocess` to documented parameters by [@abidlabs](https://github.com/abidlabs) in [PR 2293](https://github.com/gradio-app/gradio/pull/2293)
4. Update 2)key_features.md by [@voidxd](https://github.com/voidxd) in [PR 2326](https://github.com/gradio-app/gradio/pull/2326)
5. Add docs to blocks context postprocessing function by [@Ian-GL](https://github.com/Ian-GL) in [PR 2332](https://github.com/gradio-app/gradio/pull/2332)

## Testing and Infrastructure Changes

1. Website fixes and refactoring by [@aliabd](https://github.com/aliabd) in [PR 2280](https://github.com/gradio-app/gradio/pull/2280)
2. Don't deploy to spaces on release by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2313](https://github.com/gradio-app/gradio/pull/2313)

## Full Changelog:

- Website fixes and refactoring by [@aliabd](https://github.com/aliabd) in [PR 2280](https://github.com/gradio-app/gradio/pull/2280)
- Fix bug where max concurrency count is not respected in queue by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2286](https://github.com/gradio-app/gradio/pull/2286)
- Promotes `postprocess` and `preprocess` to documented parameters by [@abidlabs](https://github.com/abidlabs) in [PR 2293](https://github.com/gradio-app/gradio/pull/2293)
- Raise warning when trying to cache examples but not all inputs have examples by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2279](https://github.com/gradio-app/gradio/pull/2279)
- fix : queue could be blocked by [@SkyTNT](https://github.com/SkyTNT) in [PR 2288](https://github.com/gradio-app/gradio/pull/2288)
- Don't deploy to spaces on release by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2313](https://github.com/gradio-app/gradio/pull/2313)
- Supports `gr.update()` in example caching by [@abidlabs](https://github.com/abidlabs) in [PR 2309](https://github.com/gradio-app/gradio/pull/2309)
- Respect Upstream Queue when loading interfaces/blocks from Spaces by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2294](https://github.com/gradio-app/gradio/pull/2294)
- Clipboard fix for iframes by [@abidlabs](https://github.com/abidlabs) in [PR 2321](https://github.com/gradio-app/gradio/pull/2321)
- Sketching + Inpainting Capabilities to Gradio by [@abidlabs](https://github.com/abidlabs) in [PR 2144](https://github.com/gradio-app/gradio/pull/2144)
- Update 2)key_features.md by [@voidxd](https://github.com/voidxd) in [PR 2326](https://github.com/gradio-app/gradio/pull/2326)
- release 3.4b3 by [@abidlabs](https://github.com/abidlabs) in [PR 2328](https://github.com/gradio-app/gradio/pull/2328)
- Fix: Dataframe column headers are reset when you add a new column by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2318](https://github.com/gradio-app/gradio/pull/2318)
- Start queue when gradio is a sub application by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2319](https://github.com/gradio-app/gradio/pull/2319)
- Fix Web Tracker Script by [@aliabd](https://github.com/aliabd) in [PR 2308](https://github.com/gradio-app/gradio/pull/2308)
- Add docs to blocks context postprocessing function by [@Ian-GL](https://github.com/Ian-GL) in [PR 2332](https://github.com/gradio-app/gradio/pull/2332)
- Fix typo in iterator variable name in run_predict function by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2340](https://github.com/gradio-app/gradio/pull/2340)
- Add captions to galleries by [@aliabid94](https://github.com/aliabid94) in [PR 2284](https://github.com/gradio-app/gradio/pull/2284)
- Typeable value on gradio.Slider by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2329](https://github.com/gradio-app/gradio/pull/2329)

## Contributors Shoutout:

- [@SkyTNT](https://github.com/SkyTNT) made their first contribution in [PR 2288](https://github.com/gradio-app/gradio/pull/2288)
- [@voidxd](https://github.com/voidxd) made their first contribution in [PR 2326](https://github.com/gradio-app/gradio/pull/2326)

# Version 3.3

## New Features:

### 1. Iterative Outputs ⏳

You can now create an iterative output simply by having your function return a generator!

Here's (part of) an example that was used to generate the interface below it. [See full code](https://colab.research.google.com/drive/1m9bWS6B82CT7bw-m4L6AJR8za7fEK7Ov?usp=sharing).

```python
def predict(steps, seed):
    generator = torch.manual_seed(seed)
    for i in range(1,steps):
        yield pipeline(generator=generator, num_inference_steps=i)["sample"][0]
```

![example](https://user-images.githubusercontent.com/9021060/189086273-f5e7087d-71fa-4158-90a9-08e84da0421c.mp4)

### 2. Accordion Layout 🆕

This version of Gradio introduces a new layout component to Blocks: the Accordion. Wrap your elements in a neat, expandable layout that allows users to toggle them as needed.

Usage: ([Read the docs](https://gradio.app/docs/#accordion))

```python
with gr.Accordion("open up"):
# components here
```

![accordion](https://user-images.githubusercontent.com/9021060/189088465-f0ffd7f0-fc6a-42dc-9249-11c5e1e0529b.gif)

### 3. Skops Integration 📈

Our new integration with [skops](https://huggingface.co/blog/skops) allows you to load tabular classification and regression models directly from the [hub](https://huggingface.co/models).

Here's a classification example showing how quick it is to set up an interface for a [model](https://huggingface.co/scikit-learn/tabular-playground).

```python
import gradio as gr
gr.Interface.load("models/scikit-learn/tabular-playground").launch()
```

![187936493-5c90c01d-a6dd-400f-aa42-833a096156a1](https://user-images.githubusercontent.com/9021060/189090519-328fbcb4-120b-43c8-aa54-d6fccfa6b7e8.png)

## Bug Fixes:

No changes to highlight.

## Documentation Changes:

No changes to highlight.

## Testing and Infrastructure Changes:

No changes to highlight.

## Breaking Changes:

No changes to highlight.

## Full Changelog:

- safari fixes by [@pngwn](https://github.com/pngwn) in [PR 2138](https://github.com/gradio-app/gradio/pull/2138)
- Fix roundedness and form borders by [@aliabid94](https://github.com/aliabid94) in [PR 2147](https://github.com/gradio-app/gradio/pull/2147)
- Better processing of example data prior to creating dataset component by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2147](https://github.com/gradio-app/gradio/pull/2147)
- Show error on Connection drops by [@aliabid94](https://github.com/aliabid94) in [PR 2147](https://github.com/gradio-app/gradio/pull/2147)
- 3.2 release! by [@abidlabs](https://github.com/abidlabs) in [PR 2139](https://github.com/gradio-app/gradio/pull/2139)
- Fixed Named API Requests by [@abidlabs](https://github.com/abidlabs) in [PR 2151](https://github.com/gradio-app/gradio/pull/2151)
- Quick Fix: Cannot upload Model3D image after clearing it by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2168](https://github.com/gradio-app/gradio/pull/2168)
- Fixed misleading log when server_name is '0.0.0.0' by [@lamhoangtung](https://github.com/lamhoangtung) in [PR 2176](https://github.com/gradio-app/gradio/pull/2176)
- Keep embedded PngInfo metadata by [@cobryan05](https://github.com/cobryan05) in [PR 2170](https://github.com/gradio-app/gradio/pull/2170)
- Skops integration: Load tabular classification and regression models from the hub by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2126](https://github.com/gradio-app/gradio/pull/2126)
- Respect original filename when cached example files are downloaded by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2145](https://github.com/gradio-app/gradio/pull/2145)
- Add manual trigger to deploy to pypi by [@abidlabs](https://github.com/abidlabs) in [PR 2192](https://github.com/gradio-app/gradio/pull/2192)
- Fix bugs with gr.update by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2157](https://github.com/gradio-app/gradio/pull/2157)
- Make queue per app by [@aliabid94](https://github.com/aliabid94) in [PR 2193](https://github.com/gradio-app/gradio/pull/2193)
- Preserve Labels In Interpretation Components by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2166](https://github.com/gradio-app/gradio/pull/2166)
- Quick Fix: Multiple file download not working by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2169](https://github.com/gradio-app/gradio/pull/2169)
- use correct MIME type for js-script file by [@daspartho](https://github.com/daspartho) in [PR 2200](https://github.com/gradio-app/gradio/pull/2200)
- Add accordion component by [@aliabid94](https://github.com/aliabid94) in [PR 2208](https://github.com/gradio-app/gradio/pull/2208)

## Contributors Shoutout:

- [@lamhoangtung](https://github.com/lamhoangtung) made their first contribution in [PR 2176](https://github.com/gradio-app/gradio/pull/2176)
- [@cobryan05](https://github.com/cobryan05) made their first contribution in [PR 2170](https://github.com/gradio-app/gradio/pull/2170)
- [@daspartho](https://github.com/daspartho) made their first contribution in [PR 2200](https://github.com/gradio-app/gradio/pull/2200)

# Version 3.2

## New Features:

### 1. Improvements to Queuing 🥇

We've implemented a brand new queuing system based on **web sockets** instead of HTTP long polling. Among other things, this allows us to manage queue sizes better on Hugging Face Spaces. There are also additional queue-related parameters you can add:

- Now supports concurrent workers (parallelization)

```python
demo = gr.Interface(...)
demo.queue(concurrency_count=3)
demo.launch()
```

- Configure a maximum queue size

```python
demo = gr.Interface(...)
demo.queue(max_size=100)
demo.launch()
```

- If a user closes their tab / browser, they leave the queue, which means the demo will run faster for everyone else

### 2. Fixes to Examples

- Dataframe examples will render properly, and look much clearer in the UI: (thanks to PR #2125)

![Screen Shot 2022-08-30 at 8 29 58 PM](https://user-images.githubusercontent.com/9021060/187586561-d915bafb-f968-4966-b9a2-ef41119692b2.png)

- Image and Video thumbnails are cropped to look neater and more uniform: (thanks to PR #2109)

![Screen Shot 2022-08-30 at 8 32 15 PM](https://user-images.githubusercontent.com/9021060/187586890-56e1e4f0-1b84-42d9-a82f-911772c41030.png)

- Other fixes in PR #2131 and #2064 make it easier to design and use Examples

### 3. Component Fixes 🧱

- Specify the width and height of an image in its style tag (thanks to PR #2133)

```python
components.Image().style(height=260, width=300)
```

- Automatic conversion of videos so they are playable in the browser (thanks to PR #2003). Gradio will check if a video's format is playable in the browser and, if it isn't, will automatically convert it to a format that is (mp4).
- Pass in a json filepath to the Label component (thanks to PR #2083)
- Randomize the default value of a Slider (thanks to PR #1935)

![slider-random](https://user-images.githubusercontent.com/9021060/187596230-3db9697f-9f4d-42f5-9387-d77573513448.gif)

- Improvements to State in PR #2100

### 4. Ability to Randomize Input Sliders and Reload Data whenever the Page Loads

- In some cases, you want to be able to show a different set of input data to every user as they load the page app. For example, you might want to randomize the value of a "seed" `Slider` input. Or you might want to show a `Textbox` with the current date. We now supporting passing _functions_ as the default value in input components. When you pass in a function, it gets **re-evaluated** every time someone loads the demo, allowing you to reload / change data for different users.

Here's an example loading the current date time into an input Textbox:

```python
import gradio as gr
import datetime

with gr.Blocks() as demo:
    gr.Textbox(datetime.datetime.now)

demo.launch()
```

Note that we don't evaluate the function -- `datetime.datetime.now()` -- we pass in the function itself to get this behavior -- `datetime.datetime.now`

Because randomizing the initial value of `Slider` is a common use case, we've added a `randomize` keyword argument you can use to randomize its initial value:

```python
import gradio as gr
demo = gr.Interface(lambda x:x, gr.Slider(0, 10, randomize=True), "number")
demo.launch()
```

### 5. New Guide 🖊️

- [Gradio and W&B Integration](https://gradio.app/Gradio_and_Wandb_Integration/)

## Full Changelog:

- Reset components to original state by setting value to None by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2044](https://github.com/gradio-app/gradio/pull/2044)
- Cleaning up the way data is processed for components by [@abidlabs](https://github.com/abidlabs) in [PR 1967](https://github.com/gradio-app/gradio/pull/1967)
- version 3.1.8b by [@abidlabs](https://github.com/abidlabs) in [PR 2063](https://github.com/gradio-app/gradio/pull/2063)
- Wandb guide by [@AK391](https://github.com/AK391) in [PR 1898](https://github.com/gradio-app/gradio/pull/1898)
- Add a flagging callback to save json files to a hugging face dataset by [@chrisemezue](https://github.com/chrisemezue) in [PR 1821](https://github.com/gradio-app/gradio/pull/1821)
- Add data science demos to landing page by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2067](https://github.com/gradio-app/gradio/pull/2067)
- Hide time series + xgboost demos by default by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2079](https://github.com/gradio-app/gradio/pull/2079)
- Encourage people to keep trying when queue full by [@apolinario](https://github.com/apolinario) in [PR 2076](https://github.com/gradio-app/gradio/pull/2076)
- Updated our analytics on creation of Blocks/Interface by [@abidlabs](https://github.com/abidlabs) in [PR 2082](https://github.com/gradio-app/gradio/pull/2082)
- `Label` component now accepts file paths to `.json` files by [@abidlabs](https://github.com/abidlabs) in [PR 2083](https://github.com/gradio-app/gradio/pull/2083)
- Fix issues related to demos in Spaces by [@abidlabs](https://github.com/abidlabs) in [PR 2086](https://github.com/gradio-app/gradio/pull/2086)
- Fix TimeSeries examples not properly displayed in UI by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2064](https://github.com/gradio-app/gradio/pull/2064)
- Fix infinite requests when doing tab item select by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2070](https://github.com/gradio-app/gradio/pull/2070)
- Accept deprecated `file` route as well by [@abidlabs](https://github.com/abidlabs) in [PR 2099](https://github.com/gradio-app/gradio/pull/2099)
- Allow frontend method execution on Block.load event by [@codedealer](https://github.com/codedealer) in [PR 2108](https://github.com/gradio-app/gradio/pull/2108)
- Improvements to `State` by [@abidlabs](https://github.com/abidlabs) in [PR 2100](https://github.com/gradio-app/gradio/pull/2100)
- Catch IndexError, KeyError in video_is_playable by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 2113](https://github.com/gradio-app/gradio/pull/2113)
- Fix: Download button does not respect the filepath returned by the function by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 2073](https://github.com/gradio-app/gradio/pull/2073)
- Refactoring Layout: Adding column widths, forms, and more. by [@aliabid94](https://github.com/aliabid94) in [PR 2097](https://github.com/gradio-app/gradio/pull/2097)
- Update CONTRIBUTING.md by [@abidlabs](https://github.com/abidlabs) in [PR 2118](https://github.com/gradio-app/gradio/pull/2118)
- 2092 df ex by [@pngwn](https://github.com/pngwn) in [PR 2125](https://github.com/gradio-app/gradio/pull/2125)
- feat(samples table/gallery): Crop thumbs to square by [@ronvoluted](https://github.com/ronvoluted) in [PR 2109](https://github.com/gradio-app/gradio/pull/2109)
- Some enhancements to `gr.Examples` by [@abidlabs](https://github.com/abidlabs) in [PR 2131](https://github.com/gradio-app/gradio/pull/2131)
- Image size fix by [@aliabid94](https://github.com/aliabid94) in [PR 2133](https://github.com/gradio-app/gradio/pull/2133)

## Contributors Shoutout:

- [@chrisemezue](https://github.com/chrisemezue) made their first contribution in [PR 1821](https://github.com/gradio-app/gradio/pull/1821)
- [@apolinario](https://github.com/apolinario) made their first contribution in [PR 2076](https://github.com/gradio-app/gradio/pull/2076)
- [@codedealer](https://github.com/codedealer) made their first contribution in [PR 2108](https://github.com/gradio-app/gradio/pull/2108)

# Version 3.1

## New Features:

### 1. Embedding Demos on Any Website 💻

With PR #1444, Gradio is now distributed as a web component. This means demos can be natively embedded on websites. You'll just need to add two lines: one to load the gradio javascript, and one to link to the demos backend.

Here's a simple example that embeds the demo from a Hugging Face space:

```html
<script
	type="module"
	src="https://gradio.s3-us-west-2.amazonaws.com/3.0.18/gradio.js"
></script>
<gradio-app space="abidlabs/pytorch-image-classifier"></gradio-app>
```

But you can also embed demos that are running anywhere, you just need to link the demo to `src` instead of `space`. In fact, all the demos on the gradio website are embedded this way:

<img width="1268" alt="Screen Shot 2022-07-14 at 2 41 44 PM" src="https://user-images.githubusercontent.com/9021060/178997124-b2f05af2-c18f-4716-bf1b-cb971d012636.png">

Read more in the [Embedding Gradio Demos](https://gradio.app/embedding_gradio_demos) guide.

### 2. Reload Mode 👨‍💻

Reload mode helps developers create gradio demos faster by automatically reloading the demo whenever the code changes. It can support development on Python IDEs (VS Code, PyCharm, etc), the terminal, as well as Jupyter notebooks.

If your demo code is in a script named `app.py`, instead of running `python app.py` you can now run `gradio app.py` and that will launch the demo in reload mode:

```bash
Launching in reload mode on: http://127.0.0.1:7860 (Press CTRL+C to quit)
Watching...
WARNING: The --reload flag should not be used in production on Windows.
```

If you're working from a Jupyter or Colab Notebook, use these magic commands instead: `%load_ext gradio` when you import gradio, and `%%blocks` in the top of the cell with the demo code. Here's an example that shows how much faster the development becomes:

![Blocks](https://user-images.githubusercontent.com/9021060/178986488-ed378cc8-5141-4330-ba41-672b676863d0.gif)

### 3. Inpainting Support on `gr.Image()` 🎨

We updated the Image component to add support for inpainting demos. It works by adding `tool="sketch"` as a parameter, that passes both an image and a sketchable mask to your prediction function.

Here's an example from the [LAMA space](https://huggingface.co/spaces/akhaliq/lama):

![FXApVlFVsAALSD-](https://user-images.githubusercontent.com/9021060/178989479-549867c8-7fb0-436a-a97d-1e91c9f5e611.jpeg)

### 4. Markdown and HTML support in Dataframes 🔢

We upgraded the Dataframe component in PR #1684 to support rendering Markdown and HTML inside the cells.

This means you can build Dataframes that look like the following:

![image (8)](https://user-images.githubusercontent.com/9021060/178991233-41cb07a5-e7a3-433e-89b8-319bc78eb9c2.png)

### 5. `gr.Examples()` for Blocks 🧱

We've added the `gr.Examples` component helper to allow you to add examples to any Blocks demo. This class is a wrapper over the `gr.Dataset` component.

<img width="1271" alt="Screen Shot 2022-07-14 at 2 23 50 PM" src="https://user-images.githubusercontent.com/9021060/178992715-c8bc7550-bc3d-4ddc-9fcb-548c159cd153.png">

gr.Examples takes two required parameters:

- `examples` which takes in a nested list
- `inputs` which takes in a component or list of components

You can read more in the [Examples docs](https://gradio.app/docs/#examples) or the [Adding Examples to your Demos guide](https://gradio.app/adding_examples_to_your_app/).

### 6. Fixes to Audio Streaming

With [PR 1828](https://github.com/gradio-app/gradio/pull/1828) we now hide the status loading animation, as well as remove the echo in streaming. Check out the [stream_audio](https://github.com/gradio-app/gradio/blob/main/demo/stream_audio/run.py) demo for more or read through our [Real Time Speech Recognition](https://gradio.app/real_time_speech_recognition/) guide.

<img width="785" alt="Screen Shot 2022-07-19 at 6 02 35 PM" src="https://user-images.githubusercontent.com/9021060/179808136-9e84502c-f9ee-4f30-b5e9-1086f678fe91.png">

## Full Changelog:

- File component: list multiple files and allow for download #1446 by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 1681](https://github.com/gradio-app/gradio/pull/1681)
- Add ColorPicker to docs by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 1768](https://github.com/gradio-app/gradio/pull/1768)
- Mock out requests in TestRequest unit tests by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 1794](https://github.com/gradio-app/gradio/pull/1794)
- Add requirements.txt and test_files to source dist by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 1817](https://github.com/gradio-app/gradio/pull/1817)
- refactor: f-string for tunneling.py by [@nhankiet](https://github.com/nhankiet) in [PR 1819](https://github.com/gradio-app/gradio/pull/1819)
- Miscellaneous formatting improvements to website by [@aliabd](https://github.com/aliabd) in [PR 1754](https://github.com/gradio-app/gradio/pull/1754)
- `integrate()` method moved to `Blocks` by [@abidlabs](https://github.com/abidlabs) in [PR 1776](https://github.com/gradio-app/gradio/pull/1776)
- Add python-3.7 tests by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 1818](https://github.com/gradio-app/gradio/pull/1818)
- Copy test dir in website dockers by [@aliabd](https://github.com/aliabd) in [PR 1827](https://github.com/gradio-app/gradio/pull/1827)
- Add info to docs on how to set default values for components by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 1788](https://github.com/gradio-app/gradio/pull/1788)
- Embedding Components on Docs by [@aliabd](https://github.com/aliabd) in [PR 1726](https://github.com/gradio-app/gradio/pull/1726)
- Remove usage of deprecated gr.inputs and gr.outputs from website by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 1796](https://github.com/gradio-app/gradio/pull/1796)
- Some cleanups to the docs page by [@abidlabs](https://github.com/abidlabs) in [PR 1822](https://github.com/gradio-app/gradio/pull/1822)

## Contributors Shoutout:

- [@nhankiet](https://github.com/nhankiet) made their first contribution in [PR 1819](https://github.com/gradio-app/gradio/pull/1819)

# Version 3.0

### 🔥 Gradio 3.0 is the biggest update to the library, ever.

## New Features:

### 1. Blocks 🧱

Blocks is a new, low-level API that allows you to have full control over the data flows and layout of your application. It allows you to build very complex, multi-step applications. For example, you might want to:

- Group together related demos as multiple tabs in one web app
- Change the layout of your demo instead of just having all of the inputs on the left and outputs on the right
- Have multi-step interfaces, in which the output of one model becomes the input to the next model, or have more flexible data flows in general
- Change a component's properties (for example, the choices in a Dropdown) or its visibility based on user input

Here's a simple example that creates the demo below it:

```python
import gradio as gr

def update(name):
    return f"Welcome to Gradio, {name}!"

demo = gr.Blocks()

with demo:
    gr.Markdown(
    """
    # Hello World!
    Start typing below to see the output.
    """)
    inp = gr.Textbox(placeholder="What is your name?")
    out = gr.Textbox()

    inp.change(fn=update,
               inputs=inp,
               outputs=out)

demo.launch()
```

![hello-blocks](https://user-images.githubusercontent.com/9021060/168684108-78cbd24b-e6bd-4a04-a8d9-20d535203434.gif)

Read our [Introduction to Blocks](http://gradio.app/introduction_to_blocks/) guide for more, and join the 🎈 [Gradio Blocks Party](https://huggingface.co/spaces/Gradio-Blocks/README)!

### 2. Our Revamped Design 🎨

We've upgraded our design across the entire library: from components, and layouts all the way to dark mode.

![kitchen_sink](https://user-images.githubusercontent.com/9021060/168686333-7a6e3096-3e23-4309-abf2-5cd7736e0463.gif)

### 3. A New Website 💻

We've upgraded [gradio.app](https://gradio.app) to make it cleaner, faster and easier to use. Our docs now come with components and demos embedded directly on the page. So you can quickly get up to speed with what you're looking for.

![website](https://user-images.githubusercontent.com/9021060/168687191-10d6a3bd-101f-423a-8193-48f47a5e077d.gif)

### 4. New Components: Model3D, Dataset, and More..

We've introduced a lot of new components in `3.0`, including `Model3D`, `Dataset`, `Markdown`, `Button` and `Gallery`. You can find all the components and play around with them [here](https://gradio.app/docs/#components).

![Model3d](https://user-images.githubusercontent.com/9021060/168689062-6ad77151-8cc5-467d-916c-f7c78e52ec0c.gif)

## Full Changelog:

- Gradio dash fe by [@pngwn](https://github.com/pngwn) in [PR 807](https://github.com/gradio-app/gradio/pull/807)
- Blocks components by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 765](https://github.com/gradio-app/gradio/pull/765)
- Blocks components V2 by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 843](https://github.com/gradio-app/gradio/pull/843)
- Blocks-Backend-Events by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 844](https://github.com/gradio-app/gradio/pull/844)
- Interfaces from Blocks by [@aliabid94](https://github.com/aliabid94) in [PR 849](https://github.com/gradio-app/gradio/pull/849)
- Blocks dev by [@aliabid94](https://github.com/aliabid94) in [PR 853](https://github.com/gradio-app/gradio/pull/853)
- Started updating demos to use the new `gradio.components` syntax by [@abidlabs](https://github.com/abidlabs) in [PR 848](https://github.com/gradio-app/gradio/pull/848)
- add test infra + add browser tests to CI by [@pngwn](https://github.com/pngwn) in [PR 852](https://github.com/gradio-app/gradio/pull/852)
- 854 textbox by [@pngwn](https://github.com/pngwn) in [PR 859](https://github.com/gradio-app/gradio/pull/859)
- Getting old Python unit tests to pass on `blocks-dev` by [@abidlabs](https://github.com/abidlabs) in [PR 861](https://github.com/gradio-app/gradio/pull/861)
- initialise chatbot with empty array of messages by [@pngwn](https://github.com/pngwn) in [PR 867](https://github.com/gradio-app/gradio/pull/867)
- add test for output to input by [@pngwn](https://github.com/pngwn) in [PR 866](https://github.com/gradio-app/gradio/pull/866)
- More Interface -> Blocks features by [@aliabid94](https://github.com/aliabid94) in [PR 864](https://github.com/gradio-app/gradio/pull/864)
- Fixing external.py in blocks-dev to reflect the new HF Spaces paths by [@abidlabs](https://github.com/abidlabs) in [PR 879](https://github.com/gradio-app/gradio/pull/879)
- backend_default_value_refactoring by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 871](https://github.com/gradio-app/gradio/pull/871)
- fix default_value by [@pngwn](https://github.com/pngwn) in [PR 869](https://github.com/gradio-app/gradio/pull/869)
- fix buttons by [@aliabid94](https://github.com/aliabid94) in [PR 883](https://github.com/gradio-app/gradio/pull/883)
- Checking and updating more demos to use 3.0 syntax by [@abidlabs](https://github.com/abidlabs) in [PR 892](https://github.com/gradio-app/gradio/pull/892)
- Blocks Tests by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 902](https://github.com/gradio-app/gradio/pull/902)
- Interface fix by [@pngwn](https://github.com/pngwn) in [PR 901](https://github.com/gradio-app/gradio/pull/901)
- Quick fix: Issue 893 by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 907](https://github.com/gradio-app/gradio/pull/907)
- 3d Image Component by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 775](https://github.com/gradio-app/gradio/pull/775)
- fix endpoint url in prod by [@pngwn](https://github.com/pngwn) in [PR 911](https://github.com/gradio-app/gradio/pull/911)
- rename Model3d to Image3D by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 912](https://github.com/gradio-app/gradio/pull/912)
- update pypi to 2.9.1 by [@abidlabs](https://github.com/abidlabs) in [PR 916](https://github.com/gradio-app/gradio/pull/916)
- blocks-with-fix by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 917](https://github.com/gradio-app/gradio/pull/917)
- Restore Interpretation, Live, Auth, Queueing by [@aliabid94](https://github.com/aliabid94) in [PR 915](https://github.com/gradio-app/gradio/pull/915)
- Allow `Blocks` instances to be used like a `Block` in other `Blocks` by [@abidlabs](https://github.com/abidlabs) in [PR 919](https://github.com/gradio-app/gradio/pull/919)
- Redesign 1 by [@pngwn](https://github.com/pngwn) in [PR 918](https://github.com/gradio-app/gradio/pull/918)
- blocks-components-tests by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 904](https://github.com/gradio-app/gradio/pull/904)
- fix unit + browser tests by [@pngwn](https://github.com/pngwn) in [PR 926](https://github.com/gradio-app/gradio/pull/926)
- blocks-move-test-data by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 927](https://github.com/gradio-app/gradio/pull/927)
- remove debounce from form inputs by [@pngwn](https://github.com/pngwn) in [PR 932](https://github.com/gradio-app/gradio/pull/932)
- reimplement webcam video by [@pngwn](https://github.com/pngwn) in [PR 928](https://github.com/gradio-app/gradio/pull/928)
- blocks-move-test-data by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 941](https://github.com/gradio-app/gradio/pull/941)
- allow audio components to take a string value by [@pngwn](https://github.com/pngwn) in [PR 930](https://github.com/gradio-app/gradio/pull/930)
- static mode for textbox by [@pngwn](https://github.com/pngwn) in [PR 929](https://github.com/gradio-app/gradio/pull/929)
- fix file upload text by [@pngwn](https://github.com/pngwn) in [PR 931](https://github.com/gradio-app/gradio/pull/931)
- tabbed-interface-rewritten by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 958](https://github.com/gradio-app/gradio/pull/958)
- Gan demo fix by [@abidlabs](https://github.com/abidlabs) in [PR 965](https://github.com/gradio-app/gradio/pull/965)
- Blocks analytics by [@abidlabs](https://github.com/abidlabs) in [PR 947](https://github.com/gradio-app/gradio/pull/947)
- Blocks page load by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 963](https://github.com/gradio-app/gradio/pull/963)
- add frontend for page load events by [@pngwn](https://github.com/pngwn) in [PR 967](https://github.com/gradio-app/gradio/pull/967)
- fix i18n and some tweaks by [@pngwn](https://github.com/pngwn) in [PR 966](https://github.com/gradio-app/gradio/pull/966)
- add jinja2 to reqs by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 969](https://github.com/gradio-app/gradio/pull/969)
- Cleaning up `Launchable()` by [@abidlabs](https://github.com/abidlabs) in [PR 968](https://github.com/gradio-app/gradio/pull/968)
- Fix #944 by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 971](https://github.com/gradio-app/gradio/pull/971)
- New Blocks Demo: neural instrument cloning by [@abidlabs](https://github.com/abidlabs) in [PR 975](https://github.com/gradio-app/gradio/pull/975)
- Add huggingface_hub client library by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 973](https://github.com/gradio-app/gradio/pull/973)
- State and variables by [@aliabid94](https://github.com/aliabid94) in [PR 977](https://github.com/gradio-app/gradio/pull/977)
- update-components by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 986](https://github.com/gradio-app/gradio/pull/986)
- ensure dataframe updates as expected by [@pngwn](https://github.com/pngwn) in [PR 981](https://github.com/gradio-app/gradio/pull/981)
- test-guideline by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 990](https://github.com/gradio-app/gradio/pull/990)
- Issue #785: add footer by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 972](https://github.com/gradio-app/gradio/pull/972)
- indentation fix by [@abidlabs](https://github.com/abidlabs) in [PR 993](https://github.com/gradio-app/gradio/pull/993)
- missing quote by [@aliabd](https://github.com/aliabd) in [PR 996](https://github.com/gradio-app/gradio/pull/996)
- added interactive parameter to components by [@abidlabs](https://github.com/abidlabs) in [PR 992](https://github.com/gradio-app/gradio/pull/992)
- custom-components by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 985](https://github.com/gradio-app/gradio/pull/985)
- Refactor component shortcuts by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 995](https://github.com/gradio-app/gradio/pull/995)
- Plot Component by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 805](https://github.com/gradio-app/gradio/pull/805)
- updated PyPi version to 2.9.2 by [@abidlabs](https://github.com/abidlabs) in [PR 1002](https://github.com/gradio-app/gradio/pull/1002)
- Release 2.9.3 by [@abidlabs](https://github.com/abidlabs) in [PR 1003](https://github.com/gradio-app/gradio/pull/1003)
- Image3D Examples Fix by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 1001](https://github.com/gradio-app/gradio/pull/1001)
- release 2.9.4 by [@abidlabs](https://github.com/abidlabs) in [PR 1006](https://github.com/gradio-app/gradio/pull/1006)
- templates import hotfix by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1008](https://github.com/gradio-app/gradio/pull/1008)
- Progress indicator bar by [@aliabid94](https://github.com/aliabid94) in [PR 997](https://github.com/gradio-app/gradio/pull/997)
- Fixed image input for absolute path by [@JefferyChiang](https://github.com/JefferyChiang) in [PR 1004](https://github.com/gradio-app/gradio/pull/1004)
- Model3D + Plot Components by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 1010](https://github.com/gradio-app/gradio/pull/1010)
- Gradio Guides: Creating CryptoPunks with GANs by [@NimaBoscarino](https://github.com/NimaBoscarino) in [PR 1000](https://github.com/gradio-app/gradio/pull/1000)
- [BIG PR] Gradio blocks & redesigned components by [@abidlabs](https://github.com/abidlabs) in [PR 880](https://github.com/gradio-app/gradio/pull/880)
- fixed failing test on main by [@abidlabs](https://github.com/abidlabs) in [PR 1023](https://github.com/gradio-app/gradio/pull/1023)
- Use smaller ASR model in external test by [@abidlabs](https://github.com/abidlabs) in [PR 1024](https://github.com/gradio-app/gradio/pull/1024)
- updated PyPi version to 2.9.0b by [@abidlabs](https://github.com/abidlabs) in [PR 1026](https://github.com/gradio-app/gradio/pull/1026)
- Fixing import issues so that the package successfully installs on colab notebooks by [@abidlabs](https://github.com/abidlabs) in [PR 1027](https://github.com/gradio-app/gradio/pull/1027)
- Update website tracker slackbot by [@aliabd](https://github.com/aliabd) in [PR 1037](https://github.com/gradio-app/gradio/pull/1037)
- textbox-autoheight by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1009](https://github.com/gradio-app/gradio/pull/1009)
- Model3D Examples fixes by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 1035](https://github.com/gradio-app/gradio/pull/1035)
- GAN Gradio Guide: Adjustments to iframe heights by [@NimaBoscarino](https://github.com/NimaBoscarino) in [PR 1042](https://github.com/gradio-app/gradio/pull/1042)
- added better default labels to form components by [@abidlabs](https://github.com/abidlabs) in [PR 1040](https://github.com/gradio-app/gradio/pull/1040)
- Slackbot web tracker fix by [@aliabd](https://github.com/aliabd) in [PR 1043](https://github.com/gradio-app/gradio/pull/1043)
- Plot fixes by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 1044](https://github.com/gradio-app/gradio/pull/1044)
- Small fixes to the demos by [@abidlabs](https://github.com/abidlabs) in [PR 1030](https://github.com/gradio-app/gradio/pull/1030)
- fixing demo issue with website by [@aliabd](https://github.com/aliabd) in [PR 1047](https://github.com/gradio-app/gradio/pull/1047)
- [hotfix] HighlightedText by [@aliabid94](https://github.com/aliabid94) in [PR 1046](https://github.com/gradio-app/gradio/pull/1046)
- Update text by [@ronvoluted](https://github.com/ronvoluted) in [PR 1050](https://github.com/gradio-app/gradio/pull/1050)
- Update CONTRIBUTING.md by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1052](https://github.com/gradio-app/gradio/pull/1052)
- fix(ui): Increase contrast for footer by [@ronvoluted](https://github.com/ronvoluted) in [PR 1048](https://github.com/gradio-app/gradio/pull/1048)
- UI design update by [@gary149](https://github.com/gary149) in [PR 1041](https://github.com/gradio-app/gradio/pull/1041)
- updated PyPi version to 2.9.0b8 by [@abidlabs](https://github.com/abidlabs) in [PR 1059](https://github.com/gradio-app/gradio/pull/1059)
- Running, testing, and fixing demos by [@abidlabs](https://github.com/abidlabs) in [PR 1060](https://github.com/gradio-app/gradio/pull/1060)
- Form layout by [@pngwn](https://github.com/pngwn) in [PR 1054](https://github.com/gradio-app/gradio/pull/1054)
- inputless-interfaces by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1038](https://github.com/gradio-app/gradio/pull/1038)
- Update PULL_REQUEST_TEMPLATE.md by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1068](https://github.com/gradio-app/gradio/pull/1068)
- Upgrading node memory to 4gb in website Docker by [@aliabd](https://github.com/aliabd) in [PR 1069](https://github.com/gradio-app/gradio/pull/1069)
- Website reload error by [@aliabd](https://github.com/aliabd) in [PR 1079](https://github.com/gradio-app/gradio/pull/1079)
- fixed favicon issue by [@abidlabs](https://github.com/abidlabs) in [PR 1064](https://github.com/gradio-app/gradio/pull/1064)
- remove-queue-from-events by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1056](https://github.com/gradio-app/gradio/pull/1056)
- Enable vertex colors for OBJs files by [@radames](https://github.com/radames) in [PR 1074](https://github.com/gradio-app/gradio/pull/1074)
- Dark text by [@ronvoluted](https://github.com/ronvoluted) in [PR 1049](https://github.com/gradio-app/gradio/pull/1049)
- Scroll to output by [@pngwn](https://github.com/pngwn) in [PR 1077](https://github.com/gradio-app/gradio/pull/1077)
- Explicitly list pnpm version 6 in contributing guide by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 1085](https://github.com/gradio-app/gradio/pull/1085)
- hotfix for encrypt issue by [@abidlabs](https://github.com/abidlabs) in [PR 1096](https://github.com/gradio-app/gradio/pull/1096)
- Release 2.9b9 by [@abidlabs](https://github.com/abidlabs) in [PR 1098](https://github.com/gradio-app/gradio/pull/1098)
- tweak node circleci settings by [@pngwn](https://github.com/pngwn) in [PR 1091](https://github.com/gradio-app/gradio/pull/1091)
- Website Reload Error by [@aliabd](https://github.com/aliabd) in [PR 1099](https://github.com/gradio-app/gradio/pull/1099)
- Website Reload: README in demos docker by [@aliabd](https://github.com/aliabd) in [PR 1100](https://github.com/gradio-app/gradio/pull/1100)
- Flagging fixes by [@abidlabs](https://github.com/abidlabs) in [PR 1081](https://github.com/gradio-app/gradio/pull/1081)
- Backend for optional labels by [@abidlabs](https://github.com/abidlabs) in [PR 1080](https://github.com/gradio-app/gradio/pull/1080)
- Optional labels fe by [@pngwn](https://github.com/pngwn) in [PR 1105](https://github.com/gradio-app/gradio/pull/1105)
- clean-deprecated-parameters by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1090](https://github.com/gradio-app/gradio/pull/1090)
- Blocks rendering fix by [@abidlabs](https://github.com/abidlabs) in [PR 1102](https://github.com/gradio-app/gradio/pull/1102)
- Redos #1106 by [@abidlabs](https://github.com/abidlabs) in [PR 1112](https://github.com/gradio-app/gradio/pull/1112)
- Interface types: handle input-only, output-only, and unified interfaces by [@abidlabs](https://github.com/abidlabs) in [PR 1108](https://github.com/gradio-app/gradio/pull/1108)
- Hotfix + New pypi release 2.9b11 by [@abidlabs](https://github.com/abidlabs) in [PR 1118](https://github.com/gradio-app/gradio/pull/1118)
- issue-checkbox by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1122](https://github.com/gradio-app/gradio/pull/1122)
- issue-checkbox-hotfix by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1127](https://github.com/gradio-app/gradio/pull/1127)
- Fix demos in website by [@aliabd](https://github.com/aliabd) in [PR 1130](https://github.com/gradio-app/gradio/pull/1130)
- Guide for Gradio ONNX model zoo on Huggingface by [@AK391](https://github.com/AK391) in [PR 1073](https://github.com/gradio-app/gradio/pull/1073)
- ONNX guide fixes by [@aliabd](https://github.com/aliabd) in [PR 1131](https://github.com/gradio-app/gradio/pull/1131)
- Stacked form inputs css by [@gary149](https://github.com/gary149) in [PR 1134](https://github.com/gradio-app/gradio/pull/1134)
- made default value in textbox empty string by [@abidlabs](https://github.com/abidlabs) in [PR 1135](https://github.com/gradio-app/gradio/pull/1135)
- Examples UI by [@gary149](https://github.com/gary149) in [PR 1121](https://github.com/gradio-app/gradio/pull/1121)
- Chatbot custom color support by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 1092](https://github.com/gradio-app/gradio/pull/1092)
- highlighted text colors by [@pngwn](https://github.com/pngwn) in [PR 1119](https://github.com/gradio-app/gradio/pull/1119)
- pin to pnpm 6 for now by [@pngwn](https://github.com/pngwn) in [PR 1147](https://github.com/gradio-app/gradio/pull/1147)
- Restore queue in Blocks by [@aliabid94](https://github.com/aliabid94) in [PR 1137](https://github.com/gradio-app/gradio/pull/1137)
- add select event for tabitems by [@pngwn](https://github.com/pngwn) in [PR 1154](https://github.com/gradio-app/gradio/pull/1154)
- max_lines + autoheight for textbox by [@pngwn](https://github.com/pngwn) in [PR 1153](https://github.com/gradio-app/gradio/pull/1153)
- use color palette for chatbot by [@pngwn](https://github.com/pngwn) in [PR 1152](https://github.com/gradio-app/gradio/pull/1152)
- Timeseries improvements by [@pngwn](https://github.com/pngwn) in [PR 1149](https://github.com/gradio-app/gradio/pull/1149)
- move styling for interface panels to frontend by [@pngwn](https://github.com/pngwn) in [PR 1146](https://github.com/gradio-app/gradio/pull/1146)
- html tweaks by [@pngwn](https://github.com/pngwn) in [PR 1145](https://github.com/gradio-app/gradio/pull/1145)
- Issue #768: Support passing none to resize and crop image by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 1144](https://github.com/gradio-app/gradio/pull/1144)
- image gallery component + img css by [@aliabid94](https://github.com/aliabid94) in [PR 1140](https://github.com/gradio-app/gradio/pull/1140)
- networking tweak by [@abidlabs](https://github.com/abidlabs) in [PR 1143](https://github.com/gradio-app/gradio/pull/1143)
- Allow enabling queue per event listener by [@aliabid94](https://github.com/aliabid94) in [PR 1155](https://github.com/gradio-app/gradio/pull/1155)
- config hotfix and v. 2.9b23 by [@abidlabs](https://github.com/abidlabs) in [PR 1158](https://github.com/gradio-app/gradio/pull/1158)
- Custom JS calls by [@aliabid94](https://github.com/aliabid94) in [PR 1082](https://github.com/gradio-app/gradio/pull/1082)
- Small fixes: queue default fix, ffmpeg installation message by [@abidlabs](https://github.com/abidlabs) in [PR 1159](https://github.com/gradio-app/gradio/pull/1159)
- formatting by [@abidlabs](https://github.com/abidlabs) in [PR 1161](https://github.com/gradio-app/gradio/pull/1161)
- enable flex grow for gr-box by [@radames](https://github.com/radames) in [PR 1165](https://github.com/gradio-app/gradio/pull/1165)
- 1148 loading by [@pngwn](https://github.com/pngwn) in [PR 1164](https://github.com/gradio-app/gradio/pull/1164)
- Put enable_queue kwarg back in launch() by [@aliabid94](https://github.com/aliabid94) in [PR 1167](https://github.com/gradio-app/gradio/pull/1167)
- A few small fixes by [@abidlabs](https://github.com/abidlabs) in [PR 1171](https://github.com/gradio-app/gradio/pull/1171)
- Hotfix for dropdown component by [@abidlabs](https://github.com/abidlabs) in [PR 1172](https://github.com/gradio-app/gradio/pull/1172)
- use secondary buttons in interface by [@pngwn](https://github.com/pngwn) in [PR 1173](https://github.com/gradio-app/gradio/pull/1173)
- 1183 component height by [@pngwn](https://github.com/pngwn) in [PR 1185](https://github.com/gradio-app/gradio/pull/1185)
- 962 dataframe by [@pngwn](https://github.com/pngwn) in [PR 1186](https://github.com/gradio-app/gradio/pull/1186)
- update-contributing by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1188](https://github.com/gradio-app/gradio/pull/1188)
- Table tweaks by [@pngwn](https://github.com/pngwn) in [PR 1195](https://github.com/gradio-app/gradio/pull/1195)
- wrap tab content in column by [@pngwn](https://github.com/pngwn) in [PR 1200](https://github.com/gradio-app/gradio/pull/1200)
- WIP: Add dark mode support by [@gary149](https://github.com/gary149) in [PR 1187](https://github.com/gradio-app/gradio/pull/1187)
- Restored /api/predict/ endpoint for Interfaces by [@abidlabs](https://github.com/abidlabs) in [PR 1199](https://github.com/gradio-app/gradio/pull/1199)
- hltext-label by [@pngwn](https://github.com/pngwn) in [PR 1204](https://github.com/gradio-app/gradio/pull/1204)
- add copy functionality to json by [@pngwn](https://github.com/pngwn) in [PR 1205](https://github.com/gradio-app/gradio/pull/1205)
- Update component config by [@aliabid94](https://github.com/aliabid94) in [PR 1089](https://github.com/gradio-app/gradio/pull/1089)
- fix placeholder prompt by [@pngwn](https://github.com/pngwn) in [PR 1215](https://github.com/gradio-app/gradio/pull/1215)
- ensure webcam video value is propagated correctly by [@pngwn](https://github.com/pngwn) in [PR 1218](https://github.com/gradio-app/gradio/pull/1218)
- Automatic word-break in highlighted text, combine_adjacent support by [@aliabid94](https://github.com/aliabid94) in [PR 1209](https://github.com/gradio-app/gradio/pull/1209)
- async-function-support by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1190](https://github.com/gradio-app/gradio/pull/1190)
- Sharing fix for assets by [@aliabid94](https://github.com/aliabid94) in [PR 1208](https://github.com/gradio-app/gradio/pull/1208)
- Hotfixes for course demos by [@abidlabs](https://github.com/abidlabs) in [PR 1222](https://github.com/gradio-app/gradio/pull/1222)
- Allow Custom CSS by [@aliabid94](https://github.com/aliabid94) in [PR 1170](https://github.com/gradio-app/gradio/pull/1170)
- share-hotfix by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1226](https://github.com/gradio-app/gradio/pull/1226)
- tweaks by [@pngwn](https://github.com/pngwn) in [PR 1229](https://github.com/gradio-app/gradio/pull/1229)
- white space for class concatenation by [@radames](https://github.com/radames) in [PR 1228](https://github.com/gradio-app/gradio/pull/1228)
- Tweaks by [@pngwn](https://github.com/pngwn) in [PR 1230](https://github.com/gradio-app/gradio/pull/1230)
- css tweaks by [@pngwn](https://github.com/pngwn) in [PR 1235](https://github.com/gradio-app/gradio/pull/1235)
- ensure defaults height match for media inputs by [@pngwn](https://github.com/pngwn) in [PR 1236](https://github.com/gradio-app/gradio/pull/1236)
- Default Label label value by [@radames](https://github.com/radames) in [PR 1239](https://github.com/gradio-app/gradio/pull/1239)
- update-shortcut-syntax by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1234](https://github.com/gradio-app/gradio/pull/1234)
- Update version.txt by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1244](https://github.com/gradio-app/gradio/pull/1244)
- Layout bugs by [@pngwn](https://github.com/pngwn) in [PR 1246](https://github.com/gradio-app/gradio/pull/1246)
- Update demo by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1253](https://github.com/gradio-app/gradio/pull/1253)
- Button default name by [@FarukOzderim](https://github.com/FarukOzderim) in [PR 1243](https://github.com/gradio-app/gradio/pull/1243)
- Labels spacing by [@gary149](https://github.com/gary149) in [PR 1254](https://github.com/gradio-app/gradio/pull/1254)
- add global loader for gradio app by [@pngwn](https://github.com/pngwn) in [PR 1251](https://github.com/gradio-app/gradio/pull/1251)
- ui apis for dalle-mini by [@pngwn](https://github.com/pngwn) in [PR 1258](https://github.com/gradio-app/gradio/pull/1258)
- Add precision to Number, backend only by [@freddyaboulton](https://github.com/freddyaboulton) in [PR 1125](https://github.com/gradio-app/gradio/pull/1125)
- Website Design Changes by [@abidlabs](https://github.com/abidlabs) in [PR 1015](https://github.com/gradio-app/gradio/pull/1015)
- Small fixes for multiple demos compatible with 3.0 by [@radames](https://github.com/radames) in [PR 1257](https://github.com/gradio-app/gradio/pull/1257)
- Issue #1160: Model 3D component not destroyed correctly by [@dawoodkhan82](https://github.com/dawoodkhan82) in [PR 1219](https://github.com/gradio-app/gradio/pull/1219)
- Fixes to components by [@abidlabs](https://github.com/abidlabs) in [PR 1260](https://github.com/gradio-app/gradio/pull/1260)
- layout docs by [@abidlabs](https://github.com/abidlabs) in [PR 1263](https://github.com/gradio-app/gradio/pull/1263)
- Static forms by [@pngwn](https://github.com/pngwn) in [PR 1264](https://github.com/gradio-app/gradio/pull/1264)
- Cdn assets by [@pngwn](https://github.com/pngwn) in [PR 1265](https://github.com/gradio-app/gradio/pull/1265)
- update logo by [@gary149](https://github.com/gary149) in [PR 1266](https://github.com/gradio-app/gradio/pull/1266)
- fix slider by [@aliabid94](https://github.com/aliabid94) in [PR 1268](https://github.com/gradio-app/gradio/pull/1268)
- maybe fix auth in iframes by [@pngwn](https://github.com/pngwn) in [PR 1261](https://github.com/gradio-app/gradio/pull/1261)
- Improves "Getting Started" guide by [@abidlabs](https://github.com/abidlabs) in [PR 1269](https://github.com/gradio-app/gradio/pull/1269)
- Add embedded demos to website by [@aliabid94](https://github.com/aliabid94) in [PR 1270](https://github.com/gradio-app/gradio/pull/1270)
- Label hotfixes by [@abidlabs](https://github.com/abidlabs) in [PR 1281](https://github.com/gradio-app/gradio/pull/1281)
- General tweaks by [@pngwn](https://github.com/pngwn) in [PR 1276](https://github.com/gradio-app/gradio/pull/1276)
- only affect links within the document by [@pngwn](https://github.com/pngwn) in [PR 1282](https://github.com/gradio-app/gradio/pull/1282)
- release 3.0b9 by [@abidlabs](https://github.com/abidlabs) in [PR 1283](https://github.com/gradio-app/gradio/pull/1283)
- Dm by [@pngwn](https://github.com/pngwn) in [PR 1284](https://github.com/gradio-app/gradio/pull/1284)
- Website fixes by [@aliabd](https://github.com/aliabd) in [PR 1286](https://github.com/gradio-app/gradio/pull/1286)
- Create Streamables by [@aliabid94](https://github.com/aliabid94) in [PR 1279](https://github.com/gradio-app/gradio/pull/1279)
- ensure table works on mobile by [@pngwn](https://github.com/pngwn) in [PR 1277](https://github.com/gradio-app/gradio/pull/1277)
- changes by [@aliabid94](https://github.com/aliabid94) in [PR 1287](https://github.com/gradio-app/gradio/pull/1287)
- demo alignment on landing page by [@aliabd](https://github.com/aliabd) in [PR 1288](https://github.com/gradio-app/gradio/pull/1288)
- New meta img by [@aliabd](https://github.com/aliabd) in [PR 1289](https://github.com/gradio-app/gradio/pull/1289)
- updated PyPi version to 3.0 by [@abidlabs](https://github.com/abidlabs) in [PR 1290](https://github.com/gradio-app/gradio/pull/1290)
- Fix site by [@aliabid94](https://github.com/aliabid94) in [PR 1291](https://github.com/gradio-app/gradio/pull/1291)
- Mobile responsive guides by [@aliabd](https://github.com/aliabd) in [PR 1293](https://github.com/gradio-app/gradio/pull/1293)
- Update readme by [@abidlabs](https://github.com/abidlabs) in [PR 1292](https://github.com/gradio-app/gradio/pull/1292)
- gif by [@abidlabs](https://github.com/abidlabs) in [PR 1296](https://github.com/gradio-app/gradio/pull/1296)
- Allow decoding headerless b64 string [@1lint](https://github.com/1lint) in [PR 4031](https://github.com/gradio-app/gradio/pull/4031)

## Contributors Shoutout:

- [@JefferyChiang](https://github.com/JefferyChiang) made their first contribution in [PR 1004](https://github.com/gradio-app/gradio/pull/1004)
- [@NimaBoscarino](https://github.com/NimaBoscarino) made their first contribution in [PR 1000](https://github.com/gradio-app/gradio/pull/1000)
- [@ronvoluted](https://github.com/ronvoluted) made their first contribution in [PR 1050](https://github.com/gradio-app/gradio/pull/1050)
- [@radames](https://github.com/radames) made their first contribution in [PR 1074](https://github.com/gradio-app/gradio/pull/1074)
- [@freddyaboulton](https://github.com/freddyaboulton) made their first contribution in [PR 1085](https://github.com/gradio-app/gradio/pull/1085)
