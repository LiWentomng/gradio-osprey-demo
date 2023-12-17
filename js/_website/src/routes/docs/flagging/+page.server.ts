import docs_json from "../docs.json";
import Demos from "../../../components/Demos.svelte";
import DocsNav from "../../../components/DocsNav.svelte";
import FunctionDoc from "../../../components/FunctionDoc.svelte";
import Prism from "prismjs";
import "prismjs/components/prism-python";
import { make_slug_processor } from "../../../utils";

let language = "python";

let docs: { [key: string]: any } = docs_json.docs;
let components = docs_json.docs.components;
let helpers = docs_json.docs.helpers;
let routes = docs_json.docs.routes;
let py_client = docs_json.docs["py-client"];

const COLOR_SETS = [
	["from-green-100", "to-green-50"],
	["from-yellow-100", "to-yellow-50"],
	["from-red-100", "to-red-50"],
	["from-blue-100", "to-blue-50"],
	["from-pink-100", "to-pink-50"],
	["from-purple-100", "to-purple-50"]
];

export async function load() {
	let objs = [
		docs.building.simplecsvlogger,
		docs.building.csvlogger,
		docs.building.huggingfacedatasetsaver
	];
	let headers = [
		["SimpleCSVLogger", "simple-csv-logger"],
		["CSVLogger", "csv-logger"],
		["HuggingFaceDatasetSaver", "hugging-face-dataset-saver"]
	];
	let method_headers: string[][] = [];
	const get_slug = make_slug_processor();

	for (let obj of objs) {
		if (obj.name) {
			obj.slug = get_slug(obj.name);
		}

		if (obj.fns && obj.fns.length) {
			obj.fns.forEach((fn: any) => {
				if (fn.name) fn.slug = get_slug(`${obj.name} ${fn.name}`);
			});
		}

		if ("demos" in obj) {
			obj.demos.forEach((demo: string[]) => {
				demo.push(
					Prism.highlight(demo[1], Prism.languages[language], "python")
				);
			});
		}
		if (obj.example) {
			obj.highlighted_example = Prism.highlight(
				obj.example,
				Prism.languages[language],
				"python"
			);
		}

		if ("fns" in obj && obj.fns.length > 0) {
			for (const fn of obj.fns) {
				if (fn.example) {
					fn.highlighted_example = Prism.highlight(
						fn.example,
						Prism.languages[language],
						"python"
					);
				}
			}
		}
	}

	let mode = "flagging";

	let description = `A Gradio Interface includes a 'Flag' button that appears underneath the output. By default, clicking on the Flag button sends the input and output data back to the machine where the gradio demo is running, and saves it to a CSV log file. But this default behavior can be changed. To set what happens when the Flag button is clicked, you pass an instance of a subclass of <em>FlaggingCallback</em> to the <em>flagging_callback</em> parameter in the <em>Interface</em> constructor. You can use one of the <em>FlaggingCallback</em> subclasses that are listed below, or you can create your own, which lets you do whatever you want with the data that is being flagged.`;

	return {
		objs,
		mode,
		description,
		components,
		helpers,
		routes,
		py_client,
		COLOR_SETS,
		headers,
		method_headers
	};
}
