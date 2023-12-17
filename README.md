# Gradio-Osprey-Demo

This is the gradio used in demo of our [Osprey](https://github.com/CircleRadon/Osprey), [Pixel Understanding with Visual Instruction Tuning](). It is an extension to official [gradio-3.36.1](https://github.com/gradio-app/gradio), which supports drawing boxes on top of an image. 

## Install

### 1. Install Node.js

We install it on Ubuntu with:

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

source ~/.bashrc # or ~/.zshrc based on which one you use

nvm install v18.16.0
```


### 2. Install ppnm

```
curl -fsSL https://get.pnpm.io/install.sh | sh -

source ~/.bashrc # or ~/.zshrc based on which one you use

pnpm --version  # check if success
```

### 3. Install gradio

```
git clone 

cd gradio-demo

bash scripts/build_frontend.sh

pip install -e .
```
## Acknowledgement

The implementation is inspired by [gradio-box](https://github.com/ShoufaChen/gradio-box) and [gradio-app/gradio#3220](https://github.com/gradio-app/gradio/pull/3220), with several modifications to `gradio-3.36.1`. Thank you for their open-source contributions!