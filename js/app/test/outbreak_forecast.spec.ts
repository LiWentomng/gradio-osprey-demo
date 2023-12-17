import { test, expect } from "@gradio/tootils";

test("selecting matplotlib should show matplotlib image and pressing clear should clear output", async ({
	page
}) => {
	await page.getByLabel("Plot Type").click();
	await page.getByRole("button", { name: "Matplotlib" }).click();
	await page.getByLabel("Month").click();
	await page.getByRole("button", { name: "January" }).click();
	await page.getByLabel("Social Distancing?").check();

	await Promise.all([
		page.click("text=Submit"),
		page.waitForResponse("**/run/predict")
	]);

	const matplotlib_img = await page.getByTestId("matplotlib").getByRole("img");
	const matplotlib_img_data = await matplotlib_img.getAttribute("src");
	await expect(matplotlib_img_data).toBeTruthy();

	await page.getByRole("button", { name: "Clear" }).click();
	await expect(matplotlib_img).toHaveCount(0);
});

test("selecting plotly should show plotly plot and pressing clear should clear output", async ({
	page
}) => {
	await page.getByLabel("Plot Type").click();
	await page.getByRole("button", { name: "Plotly" }).click();
	await page.getByLabel("Month").click();
	await page.getByRole("button", { name: "January" }).click();
	await page.getByLabel("Social Distancing?").check();

	await Promise.all([
		page.click("text=Submit"),
		page.waitForResponse("**/run/predict")
	]);
	await expect(page.locator(".js-plotly-plot")).toHaveCount(1);
	await page.getByRole("button", { name: "Clear" }).click();
	await expect(page.locator(".js-plotly-plot")).toHaveCount(0);
});

test("selecting altair should show altair plot and pressing clear should clear output", async ({
	page
}) => {
	await page.getByLabel("Plot Type").click();
	await page.getByRole("button", { name: "altair" }).click();
	await page.getByLabel("Month").click();
	await page.getByRole("button", { name: "January" }).click();
	await page.getByLabel("Social Distancing?").check();

	await Promise.all([
		page.click("text=Submit"),
		page.waitForResponse("**/run/predict")
	]);

	const altair = await page.getByTestId("altair");
	await expect(altair).toHaveCount(1);

	await page.getByRole("button", { name: "Clear" }).click();
	await expect(altair).toHaveCount(0);
});

test("switching between all 3 plot types and pressing submit should update output component to corresponding plot type", async ({
	page
}) => {
	//Matplotlib
	await page.getByLabel("Plot Type").click();
	await page.getByRole("button", { name: "Matplotlib" }).click();
	await page.getByLabel("Month").click();
	await page.getByRole("button", { name: "January" }).click();
	await page.getByLabel("Social Distancing?").check();

	await Promise.all([
		page.click("text=Submit"),
		page.waitForResponse("**/run/predict")
	]);

	const matplotlib_img = await page.getByTestId("matplotlib").getByRole("img");
	const matplotlib_img_data = await matplotlib_img.getAttribute("src");
	await expect(matplotlib_img_data).toBeTruthy();

	//Plotly
	await page.getByLabel("Plot Type").click();
	await page.getByRole("button", { name: "Plotly" }).click();

	await Promise.all([
		page.click("text=Submit"),
		page.waitForResponse("**/run/predict")
	]);
	await expect(page.locator(".js-plotly-plot")).toHaveCount(1);

	//Altair
	await page.getByLabel("Plot Type").click();
	await page.getByRole("button", { name: "Altair" }).click();

	await Promise.all([
		page.click("text=Submit"),
		page.waitForResponse("**/run/predict")
	]);
	const altair = await page.getByTestId("altair");
	await expect(altair).toHaveCount(1);
});
