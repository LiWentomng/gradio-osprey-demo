import {
	getQueriesForElement,
	prettyDOM,
	fireEvent as dtlFireEvent
} from "@testing-library/dom";
import { tick } from "svelte";
import type { SvelteComponent } from "svelte";

import type {
	queries,
	Queries,
	BoundFunction,
	EventType,
	FireObject
} from "@testing-library/dom";

const containerCache = new Map();
const componentCache = new Set();

type ComponentType<T extends SvelteComponent, Props> = new (args: {
	target: any;
	props?: Props;
}) => T;

export type RenderResult<
	C extends SvelteComponent,
	Q extends Queries = typeof queries
> = {
	container: HTMLElement;
	component: C;
	debug: (el?: HTMLElement | DocumentFragment) => void;
	unmount: () => void;
} & { [P in keyof Q]: BoundFunction<Q[P]> };

export interface RenderOptions<Q extends Queries = typeof queries> {
	container?: HTMLElement;
	queries?: Q;
}

export async function render<
	Events extends Record<string, any>,
	Props extends Record<string, any>,
	T extends SvelteComponent<Props, Events>
>(
	Component: ComponentType<T, Props> | { default: ComponentType<T, Props> },
	props?: Props
): Promise<RenderResult<T>> {
	const container = document.body;
	const target = container.appendChild(document.createElement("div"));

	const ComponentConstructor: ComponentType<T, Props> =
		//@ts-ignore
		Component.default || Component;

	const component = new ComponentConstructor({
		target,
		props
	});

	containerCache.set(container, { target, component });
	componentCache.add(component);

	component.$$.on_destroy.push(() => {
		componentCache.delete(component);
	});

	await tick();

	return {
		container,
		component,
		//@ts-ignore
		debug: (el = container): void => console.warn(prettyDOM(el)),
		unmount: (): void => {
			if (componentCache.has(component)) component.$destroy();
		},
		...getQueriesForElement(container)
	};
}

const cleanupAtContainer = (container: HTMLElement): void => {
	const { target, component } = containerCache.get(container);

	if (componentCache.has(component)) component.$destroy();

	if (target.parentNode === document.body) {
		document.body.removeChild(target);
	}

	containerCache.delete(container);
};

export function cleanup(): void {
	Array.from(containerCache.keys()).forEach(cleanupAtContainer);
}

export const fireEvent = Object.keys(dtlFireEvent).reduce((acc, key) => {
	const _key = key as EventType;
	return {
		...acc,
		[_key]: async (
			element: Document | Element | Window,
			options: object = {}
		): Promise<boolean> => {
			const event = dtlFireEvent[_key](element, options);
			await tick();
			return event;
		}
	};
}, {} as FireObject);

export type FireFunction = (
	element: Document | Element | Window,
	event: Event
) => Promise<boolean>;

export * from "@testing-library/dom";
