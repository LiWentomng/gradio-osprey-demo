import { test, expect } from "@gradio/tootils";

test("a component acts as both input and output", async ({ page }) => {
	const textbox = await page.getByLabel("Input-Output");

	await textbox.fill("test");
	await Promise.all([
		page.click("button"),
		page.waitForResponse("**/run/predict")
	]);
	await expect(await textbox).toHaveValue("tset");
});
