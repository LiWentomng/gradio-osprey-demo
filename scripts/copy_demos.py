import argparse
import os
import pathlib
import shutil
import textwrap


def copy_all_demos(source_dir: str, dest_dir: str):
    demos_to_copy = [
        "audio_debugger",
        "altair_plot",
        "blocks_essay",
        "blocks_js_methods",
        "blocks_layout",
        "blocks_mask",
        "blocks_multiple_event_triggers",
        "blocks_update",
        "calculator",
        "cancel_events",
        "chatbot_multimodal",
        "clear_components",
        "code",
        "fake_gan",
        "fake_diffusion_with_gif",
        "gender_sentence_default_interpretation",
        "image_mod_default_image",
        "image_segmentation",
        "interface_parallel_load",
        "interface_random_slider",
        "interface_series_load",
        "kitchen_sink",
        "kitchen_sink_random",
        "matrix_transpose",
        "model3D",
        "native_plots",
        "reverse_audio",
        "stt_or_tts",
        "stream_audio",
        "stream_frames",
        "video_component",
        "zip_files",
    ]
    for demo in demos_to_copy:
        shutil.copytree(
            os.path.join(source_dir, demo),
            os.path.join(dest_dir, demo),
            dirs_exist_ok=True,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Copy all demos to all_demos and update requirements"
    )
    parser.add_argument("gradio_version", type=str, help="Gradio")
    args = parser.parse_args()

    source_dir = pathlib.Path(pathlib.Path(__file__).parent, "..", "demo")
    dest_dir = pathlib.Path(
        pathlib.Path(__file__).parent, "..", "demo", "all_demos", "demos"
    )
    copy_all_demos(source_dir, dest_dir)
    reqs_file_path = pathlib.Path(
        pathlib.Path(__file__).parent, "..", "demo", "all_demos", "requirements.txt"
    )
    requirements = f"""
    {args.gradio_version}
    pypistats==1.1.0
    plotly==5.10.0
    opencv-python==4.6.0.66
    transformers==4.21.1
    torch==1.12.1
    altair
    vega_datasets
    """
    open(reqs_file_path, "w").write(textwrap.dedent(requirements))
