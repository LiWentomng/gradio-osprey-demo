import gradio as gr
from gradio.components import Markdown as md
from PIL import Image

demo = gr.Blocks()

io1a = gr.Interface(lambda x: x, gr.Image(), gr.Image())
io1b = gr.Interface(lambda x: x, gr.Image(source="webcam"), gr.Image())

io2a = gr.Interface(lambda x: x, gr.Image(source="canvas"), gr.Image())
io2b = gr.Interface(lambda x: x, gr.Sketchpad(), gr.Image())
io2c = gr.Interface(
    lambda x: x, gr.Image(source="canvas", shape=(512, 512)), gr.Image()
)

io3a = gr.Interface(
    lambda x: [x["mask"], x["image"]],
    gr.Image(source="upload", tool="sketch"),
    [gr.Image(), gr.Image()],
)

io3b = gr.Interface(
    lambda x: [x["mask"], x["image"]],
    gr.ImageMask(),
    [gr.Image(), gr.Image()],
)

io3b2 = gr.Interface(
    lambda x: [x["mask"], x["image"]],
    gr.ImageMask(),
    [gr.Image(), gr.Image()],
)

io3b3 = gr.Interface(
    lambda x: [x["mask"], x["image"]],
    gr.ImageMask(),
    [gr.Image(), gr.Image()],
)

io3c = gr.Interface(
    lambda x: [x["mask"], x["image"]],
    gr.Image(source="webcam", tool="sketch"),
    [gr.Image(), gr.Image()],
)

io4a = gr.Interface(
    lambda x: x, gr.Image(source="canvas", tool="color-sketch"), gr.Image()
)
io4b = gr.Interface(lambda x: x, gr.Paint(), gr.Image())

io5a = gr.Interface(
    lambda x: x, gr.Image(source="upload", tool="color-sketch"), gr.Image()
)
io5b = gr.Interface(lambda x: x, gr.ImagePaint(), gr.Image())
io5c = gr.Interface(
    lambda x: x, gr.Image(source="webcam", tool="color-sketch"), gr.Image()
)


def save_image(image):
    image.save("colorede.png")
    return image


img = Image.new("RGB", (512, 512), (150, 150, 150))
img.save("image.png", "PNG")

io5d = gr.Interface(
    save_image,
    gr.Image("image.png", source="upload", tool="color-sketch", type="pil"),
    gr.Image(),
)

with demo:
    md("# Different Ways to Use the Image Input Component")
    md(
        "**1a. Standalone Image Upload: `gr.Interface(lambda x: x, gr.Image(), gr.Image())`**"
    )
    io1a.render()
    md(
        "**1b. Standalone Image from Webcam: `gr.Interface(lambda x: x, gr.Image(source='webcam'), gr.Image())`**"
    )
    io1b.render()
    md(
        "**2a. Black and White Sketchpad: `gr.Interface(lambda x: x, gr.Image(source='canvas'), gr.Image())`**"
    )
    io2a.render()
    md(
        "**2b. Black and White Sketchpad: `gr.Interface(lambda x: x, gr.Sketchpad(), gr.Image())`**"
    )
    io2b.render()
    md("**2c. Black and White Sketchpad with `shape=(512,512)`**")
    io2c.render()
    md("**3a. Binary Mask with image upload:**")
    md(
        """```python
gr.Interface(
    lambda x: [x['mask'], x['image']],
    gr.Image(source='upload', tool='sketch'),
    [gr.Image(), gr.Image()],
)
```
"""
    )
    io3a.render()
    md("**3b. Binary Mask with image upload:**")
    md(
        """```python
gr.Interface(
    lambda x: [x['mask'], x['image']],
    gr.ImageMask(),
    [gr.Image(), gr.Image()],
)
```
"""
    )
    io3b.render()
    md("**3c. Binary Mask with webcam upload:**")
    md(
        """```python
gr.Interface(
    lambda x: [x['mask'], x['image']],
    gr.Image(source='webcam', tool='sketch'),
    [gr.Image(), gr.Image()],
)
```
"""
    )
    io3c.render()
    md(
        "**4a. Color Sketchpad: `gr.Interface(lambda x: x, gr.Image(source='canvas', tool='color-sketch'), gr.Image())`**"
    )
    io4a.render()
    md("**4b. Color Sketchpad: `gr.Interface(lambda x: x, gr.Paint(), gr.Image())`**")
    io4b.render()
    md(
        "**5a. Color Sketchpad with image upload: `gr.Interface(lambda x: x, gr.Image(source='upload', tool='color-sketch'), gr.Image())`**"
    )
    io5a.render()
    md(
        "**5b. Color Sketchpad with image upload: `gr.Interface(lambda x: x, gr.ImagePaint(), gr.Image())`**"
    )
    io5b.render()
    md(
        "**5c. Color Sketchpad with webcam upload: `gr.Interface(lambda x: x, gr.Image(source='webcam', tool='color-sketch'), gr.Image())`**"
    )
    io5c.render()
    md("**Tabs**")
    with gr.Tab("One"):
        io3b2.render()
    with gr.Tab("Two"):
        io3b3.render()
    md("**5d. Color Sketchpad with image upload and a default images**")
    io5d.render()

if __name__ == "__main__":
    demo.launch()
