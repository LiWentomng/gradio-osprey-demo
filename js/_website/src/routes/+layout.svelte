<script context="module" lang="ts">
	declare global {
		interface Window {
			__gradio_mode__: "app" | "website";
			__gradio_space__: string | null;
		}
	}
	import type { media_query as MQ } from "../utils";
	export let store: ReturnType<typeof MQ>;
</script>

<script lang="ts">
	import "../assets/style.css";
	import "../assets/prism.css";

	import { page } from "$app/stores";

	import Header from "../components/Header.svelte";
	import Footer from "../components/Footer.svelte";

	import { media_query } from "../utils";
	store = media_query();

	import { browser } from "$app/environment";
	if (browser) {
		window.__gradio_mode__ = "website";
	}
	import version_json from "./version.json";
	let version = version_json.version;
</script>

<svelte:head>
	<link
		href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
		rel="stylesheet"
	/>

	<script
		async
		src="https://www.googletagmanager.com/gtag/js?id=UA-156449732-1"
	></script>
	<script>
		window.dataLayer = window.dataLayer || [];
		function gtag() {
			dataLayer.push(arguments);
		}
		gtag("js", new Date());
		gtag("config", "UA-156449732-1");
	</script>

	<script
		type="module"
		src="https://gradio.s3-us-west-2.amazonaws.com/{version}/gradio.js"
	></script>
</svelte:head>

<Header />

<slot />

<Footer />
