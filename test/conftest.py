import inspect
import pathlib
from contextlib import contextmanager

import pytest
from gradio_client import Client

import gradio as gr


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "flaky: mark test as flaky. Failure will not cause te"
    )


@pytest.fixture
def test_file_dir():
    return pathlib.Path(pathlib.Path(__file__).parent, "test_files")


@pytest.fixture
def io_components():
    classes_to_check = gr.components.IOComponent.__subclasses__()
    subclasses = []

    while classes_to_check:
        subclass = classes_to_check.pop()
        children = subclass.__subclasses__()

        if children:
            classes_to_check.extend(children)
        if "value" in inspect.signature(subclass).parameters:
            subclasses.append(subclass)

    return subclasses


@pytest.fixture
def connect():
    @contextmanager
    def _connect(demo: gr.Blocks, serialize=True):
        _, local_url, _ = demo.launch(prevent_thread_lock=True)
        try:
            yield Client(local_url, serialize=serialize)
        finally:
            # A more verbose version of .close()
            # because we should set a timeout
            # the tests that call .cancel() can get stuck
            # waiting for the thread to join
            if demo.enable_queue:
                demo._queue.close()
            demo.is_running = False
            demo.server.should_exit = True
            demo.server.thread.join(timeout=1)

    return _connect
