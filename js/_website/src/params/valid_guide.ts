import guide_names_json from "../routes/guides/json/guide_names.json";
let guide_urls = guide_names_json.guide_urls;

export function match(value: string) {
	return guide_urls.some((guide: string) => guide === value);
}
