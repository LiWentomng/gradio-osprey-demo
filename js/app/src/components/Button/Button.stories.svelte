<script>
	import { Meta, Template, Story } from "@storybook/addon-svelte-csf";
	import { Button } from "@gradio/button";
</script>

<Meta
	title="Components/Button"
	component={Button}
	argTypes={{
		label: {
			control: "text",
			description: "The text to display on the button",
			name: "label",
			value: "Gradio Button"
		},
		variant: {
			options: ["primary", "secondary", "stop"],
			description: "The variant of the button",
			control: { type: "select" },
			defaultValue: "primary"
		},
		size: {
			options: ["sm", "lg"],
			description: "The size of the button",
			control: { type: "select" },
			defaultValue: "lg"
		},
		visible: {
			options: [true, false],
			description: "Sets the visibility of the button",
			control: { type: "boolean" },
			defaultValue: true
		},
		interactive: {
			options: [true, false],
			description: "If false, the button will be in a disabled state",
			control: { type: "boolean" },
			defaultValue: true
		},
		disabled: {
			options: [true, false],
			control: { type: "boolean" },
			defaultValue: false
		},
		scale: {
			options: [null, 0.5, 1, 2],
			description:
				"relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.",
			control: { type: "select" }
		}
	}}
/>

<Template let:args>
	<Button {...args}>{args.label || "Gradio Button"}</Button>
</Template>

<Story name="Primary" args={{ variant: "primary", size: "lg", scale: 1 }} />
<Story name="Secondary" args={{ variant: "secondary", size: "lg" }} />
<Story name="Stop" source args={{ variant: "stop", size: "lg" }} />
