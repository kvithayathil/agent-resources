<!DOCTYPE html><html lang="en" dir="ltr" data-theme="dark" data-has-toc data-has-sidebar class="astro-bguv2lll"> <head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><title>Hooks | Polytoken</title><link rel="canonical" href="https://docs.polytoken.dev/harness-engineering/hooks/"/><link rel="sitemap" href="/sitemap-index.xml"/><link rel="icon" href="/favicon.ico" sizes="32x32"/><link rel="icon" href="/favicon.svg" type="image/svg+xml"/><link rel="apple-touch-icon" href="/apple-touch-icon.png"/><link rel="manifest" href="/site.webmanifest"/><link rel="alternate" type="application/rss+xml" title="Polytoken Changelog" href="https://docs.polytoken.dev/rss.xml"/><link rel="shortcut icon" href="/favicon.svg" type="image/svg+xml"/><meta name="generator" content="Astro v6.4.8"/><meta name="generator" content="Starlight v0.40.0"/><meta property="og:title" content="Hooks"/><meta property="og:type" content="article"/><meta property="og:url" content="https://docs.polytoken.dev/harness-engineering/hooks/"/><meta property="og:locale" content="en"/><meta property="og:description" content="Running your own code at points in the agent loop."/><meta property="og:site_name" content="Polytoken"/><meta name="twitter:card" content="summary_large_image"/><meta name="description" content="Running your own code at points in the agent loop."/><meta name="theme-color" content="#6b88ab"/><script>
	window.StarlightThemeProvider = (() => {
		const storedTheme =
			typeof localStorage !== 'undefined' && localStorage.getItem('starlight-theme');
		const theme =
			storedTheme ||
			(window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
		document.documentElement.dataset.theme = theme === 'light' ? 'light' : 'dark';
		return {
			updatePickers(theme = storedTheme || 'auto') {
				document.querySelectorAll('starlight-theme-select').forEach((picker) => {
					const select = picker.querySelector('select');
					if (select) select.value = theme;
					/** @type {HTMLTemplateElement | null} */
					const tmpl = document.querySelector(`#theme-icons`);
					const newIcon = tmpl && tmpl.content.querySelector('.' + theme);
					if (newIcon) {
						const oldIcon = picker.querySelector('svg.label-icon');
						if (oldIcon) {
							oldIcon.replaceChildren(...newIcon.cloneNode(true).childNodes);
						}
					}
				});
			},
		};
	})();
</script><template id="theme-icons"><svg aria-hidden="true" class="light astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M5 12a1 1 0 0 0-1-1H3a1 1 0 0 0 0 2h1a1 1 0 0 0 1-1Zm.64 5-.71.71a1 1 0 0 0 0 1.41 1 1 0 0 0 1.41 0l.71-.71A1 1 0 0 0 5.64 17ZM12 5a1 1 0 0 0 1-1V3a1 1 0 0 0-2 0v1a1 1 0 0 0 1 1Zm5.66 2.34a1 1 0 0 0 .7-.29l.71-.71a1 1 0 1 0-1.41-1.41l-.66.71a1 1 0 0 0 0 1.41 1 1 0 0 0 .66.29Zm-12-.29a1 1 0 0 0 1.41 0 1 1 0 0 0 0-1.41l-.71-.71a1.004 1.004 0 1 0-1.43 1.41l.73.71ZM21 11h-1a1 1 0 0 0 0 2h1a1 1 0 0 0 0-2Zm-2.64 6A1 1 0 0 0 17 18.36l.71.71a1 1 0 0 0 1.41 0 1 1 0 0 0 0-1.41l-.76-.66ZM12 6.5a5.5 5.5 0 1 0 5.5 5.5A5.51 5.51 0 0 0 12 6.5Zm0 9a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Zm0 3.5a1 1 0 0 0-1 1v1a1 1 0 0 0 2 0v-1a1 1 0 0 0-1-1Z"/></svg><svg aria-hidden="true" class="dark astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M21.64 13a1 1 0 0 0-1.05-.14 8.049 8.049 0 0 1-3.37.73 8.15 8.15 0 0 1-8.14-8.1 8.59 8.59 0 0 1 .25-2A1 1 0 0 0 8 2.36a10.14 10.14 0 1 0 14 11.69 1 1 0 0 0-.36-1.05Zm-9.5 6.69A8.14 8.14 0 0 1 7.08 5.22v.27a10.15 10.15 0 0 0 10.14 10.14 9.784 9.784 0 0 0 2.1-.22 8.11 8.11 0 0 1-7.18 4.32v-.04Z"/></svg><svg aria-hidden="true" class="auto astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M21 14h-1V7a3 3 0 0 0-3-3H7a3 3 0 0 0-3 3v7H3a1 1 0 0 0-1 1v2a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3v-2a1 1 0 0 0-1-1ZM6 7a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v7H6V7Zm14 10a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-1h16v1Z"/></svg></template><link rel="stylesheet" href="/_astro/print.DNXP8c50.css" media="print"><link rel="stylesheet" href="/_astro/common.CEnwjwCJ.css"><script type="module" src="/_astro/page.B_tncCx8.js"></script></head> <body class="astro-bguv2lll"> <a href="#_top" class="astro-7q3lir66">Skip to content</a> <div class="page sl-flex astro-vrdttmbt"> <header class="header astro-vrdttmbt"><div class="header astro-kmkmnagf"> <div class="title-wrapper sl-flex astro-kmkmnagf"> <a href="/" class="site-title sl-flex astro-m46x6ez3">  <span class="astro-m46x6ez3" translate="no"> Polytoken </span> </a> </div> <div class="sl-flex print:hidden astro-kmkmnagf"> <site-search class="astro-kmkmnagf astro-v37mnknz" data-translations="{&quot;placeholder&quot;:&quot;Search&quot;}"> <button data-open-modal disabled aria-label="Search" aria-keyshortcuts="Control+K" class="astro-v37mnknz"> <svg aria-hidden="true" class="astro-v37mnknz astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M21.71 20.29 18 16.61A9 9 0 1 0 16.61 18l3.68 3.68a.999.999 0 0 0 1.42 0 1 1 0 0 0 0-1.39ZM11 18a7 7 0 1 1 0-14 7 7 0 0 1 0 14Z"/></svg> <span class="sl-hidden md:sl-block astro-v37mnknz" aria-hidden="true">Search</span> <kbd class="sl-hidden md:sl-flex astro-v37mnknz" style="display: none;"> <kbd class="astro-v37mnknz">Ctrl</kbd><kbd class="astro-v37mnknz">K</kbd> </kbd> </button> <dialog style="padding:0" aria-label="Search" class="astro-v37mnknz"> <div class="dialog-frame sl-flex astro-v37mnknz">  <button data-close-modal class="sl-flex md:sl-hidden astro-v37mnknz"> Cancel </button> <div class="search-container astro-v37mnknz"> <div id="starlight__search" class="astro-v37mnknz"></div> </div> </div> </dialog> </site-search>  <script>
	(() => {
		const openBtn = document.querySelector('button[data-open-modal]');
		const shortcut = openBtn?.querySelector('kbd');
		if (!openBtn || !(shortcut instanceof HTMLElement)) return;
		const platformKey = shortcut.querySelector('kbd');
		if (platformKey && /(Mac|iPhone|iPod|iPad)/i.test(navigator.platform)) {
			platformKey.textContent = '⌘';
			openBtn.setAttribute('aria-keyshortcuts', 'Meta+K');
		}
		shortcut.style.display = '';
	})();
</script> <script type="module" src="/_astro/Search.astro_astro_type_script_index_0_lang.lq3t8uE2.js"></script>  </div> <div class="sl-hidden md:sl-flex print:hidden right-group astro-kmkmnagf"> <div class="sl-flex social-icons astro-kmkmnagf"> <a href="https://discord.gg/5fhv7mxEUZ" rel="me" class="sl-flex astro-wy4te6ga"><span class="sr-only astro-wy4te6ga">Discord</span><svg aria-hidden="true" class="astro-wy4te6ga astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M20.32 4.37a19.8 19.8 0 0 0-4.93-1.51 13.78 13.78 0 0 0-.64 1.28 18.27 18.27 0 0 0-5.5 0 12.64 12.64 0 0 0-.64-1.28h-.05A19.74 19.74 0 0 0 3.64 4.4 20.26 20.26 0 0 0 .11 18.09l.02.02a19.9 19.9 0 0 0 6.04 3.03l.04-.02a14.24 14.24 0 0 0 1.23-2.03.08.08 0 0 0-.05-.07 13.1 13.1 0 0 1-1.9-.92.08.08 0 0 1 .02-.1 10.2 10.2 0 0 0 .41-.31h.04a14.2 14.2 0 0 0 12.1 0l.04.01a9.63 9.63 0 0 0 .4.32.08.08 0 0 1-.03.1 12.29 12.29 0 0 1-1.9.91.08.08 0 0 0-.02.1 15.97 15.97 0 0 0 1.27 2.01h.04a19.84 19.84 0 0 0 6.03-3.05v-.03a20.12 20.12 0 0 0-3.57-13.69ZM8.02 15.33c-1.18 0-2.16-1.08-2.16-2.42 0-1.33.96-2.42 2.16-2.42 1.21 0 2.18 1.1 2.16 2.42 0 1.34-.96 2.42-2.16 2.42Zm7.97 0c-1.18 0-2.15-1.08-2.15-2.42 0-1.33.95-2.42 2.15-2.42 1.22 0 2.18 1.1 2.16 2.42 0 1.34-.94 2.42-2.16 2.42Z"/></svg></a><a href="https://bsky.app/profile/polytoken.dev" rel="me" class="sl-flex astro-wy4te6ga"><span class="sr-only astro-wy4te6ga">Bluesky</span><svg aria-hidden="true" class="astro-wy4te6ga astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M12 10.8c-1-2.1-4-6-6.8-8C2.6 1 1.6 1.3.9 1.6.1 1.9 0 3 0 3.8c0 .7.4 5.6.6 6.4C1.4 13 4.3 14 7 13.6h.4H7c-4 .6-7.4 2-2.8 7 5 5.3 6.8-1 7.8-4.2 1 3.2 2 9.3 7.7 4.3 4.3-4.3 1.2-6.5-2.7-7a9 9 0 0 1-.4-.1h.4c2.7.3 5.6-.6 6.4-3.4.2-.8.6-5.7.6-6.4 0-.7-.1-1.9-.9-2.2-.7-.3-1.7-.7-4.3 1.2-2.8 2-5.7 5.9-6.8 8"/></svg></a> </div> <starlight-theme-select>  <label style="--sl-select-width: 6.25em" class="astro-4yphtoen"> <span class="sr-only astro-4yphtoen">Select theme</span> <svg aria-hidden="true" class="icon label-icon astro-4yphtoen astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M21 14h-1V7a3 3 0 0 0-3-3H7a3 3 0 0 0-3 3v7H3a1 1 0 0 0-1 1v2a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3v-2a1 1 0 0 0-1-1ZM6 7a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v7H6V7Zm14 10a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-1h16v1Z"/></svg> <select autocomplete="off" class="astro-4yphtoen"> <option value="dark" class="astro-4yphtoen">Dark</option><option value="light" class="astro-4yphtoen">Light</option><option value="auto" selected class="astro-4yphtoen">Auto</option> </select> <svg aria-hidden="true" class="icon caret astro-4yphtoen astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M17 9.17a1 1 0 0 0-1.41 0L12 12.71 8.46 9.17a1 1 0 1 0-1.41 1.42l4.24 4.24a1.002 1.002 0 0 0 1.42 0L17 10.59a1.002 1.002 0 0 0 0-1.42Z"/></svg> </label> </starlight-theme-select>  <script>
	StarlightThemeProvider.updatePickers();
</script> <script type="module">const r="starlight-theme",o=e=>e==="auto"||e==="dark"||e==="light"?e:"auto",c=()=>o(typeof localStorage<"u"&&localStorage.getItem(r));function n(e){typeof localStorage<"u"&&localStorage.setItem(r,e==="light"||e==="dark"?e:"")}const l=()=>matchMedia("(prefers-color-scheme: light)").matches?"light":"dark";function t(e){StarlightThemeProvider.updatePickers(e),document.documentElement.dataset.theme=e==="auto"?l():e,n(e)}matchMedia("(prefers-color-scheme: light)").addEventListener("change",()=>{c()==="auto"&&t("auto")});class s extends HTMLElement{constructor(){super(),t(c()),this.querySelector("select")?.addEventListener("change",a=>{a.currentTarget instanceof HTMLSelectElement&&t(o(a.currentTarget.value))})}}customElements.define("starlight-theme-select",s);</script> <script type="module">class s extends HTMLElement{constructor(){super();const e=this.querySelector("select");e&&(e.addEventListener("change",t=>{t.currentTarget instanceof HTMLSelectElement&&(window.location.pathname=t.currentTarget.value)}),window.addEventListener("pageshow",t=>{if(!t.persisted)return;const n=e.querySelector("option[selected]")?.index;n!==e.selectedIndex&&(e.selectedIndex=n??0)}))}}customElements.define("starlight-lang-select",s);</script> </div> </div></header> <nav class="sidebar print:hidden astro-vrdttmbt" aria-label="Main"> <starlight-menu-button class="print:hidden astro-jif73yzw"> <button aria-expanded="false" aria-label="Menu" aria-controls="starlight__sidebar" class="sl-flex md:sl-hidden astro-jif73yzw"> <svg aria-hidden="true" class="open-menu astro-jif73yzw astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M3 8h18a1 1 0 1 0 0-2H3a1 1 0 0 0 0 2Zm18 8H3a1 1 0 0 0 0 2h18a1 1 0 0 0 0-2Zm0-5H3a1 1 0 0 0 0 2h18a1 1 0 0 0 0-2Z"/></svg> <svg aria-hidden="true" class="close-menu astro-jif73yzw astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="m13.41 12 6.3-6.29a1.004 1.004 0 1 0-1.42-1.42L12 10.59l-6.29-6.3a1.004 1.004 0 0 0-1.42 1.42l6.3 6.29-6.3 6.29a1 1 0 0 0 0 1.42.998.998 0 0 0 1.42 0l6.29-6.3 6.29 6.3a.999.999 0 0 0 1.42 0 1 1 0 0 0 0-1.42L13.41 12Z"/></svg> </button> </starlight-menu-button> <script type="module">class s extends HTMLElement{constructor(){super(),this.btn=this.querySelector("button"),this.btn.addEventListener("click",()=>this.toggleExpanded());const t=this.closest("nav");t&&t.addEventListener("keyup",e=>this.closeOnEscape(e))}setExpanded(t){this.setAttribute("aria-expanded",String(t)),document.body.toggleAttribute("data-mobile-menu-expanded",t)}toggleExpanded(){this.setExpanded(this.getAttribute("aria-expanded")!=="true")}closeOnEscape(t){t.code==="Escape"&&(this.setExpanded(!1),this.btn.focus())}}customElements.define("starlight-menu-button",s);</script>  <div id="starlight__sidebar" class="sidebar-pane astro-vrdttmbt"> <div class="sidebar-content sl-flex astro-vrdttmbt"> <sl-sidebar-state-persist data-hash="02kyj35" class="astro-kku4brbg"> <script aria-hidden="true">
		(() => {
			try {
				if (!matchMedia('(min-width: 50em)').matches) return;
				/** @type {HTMLElement | null} */
				const target = document.querySelector('sl-sidebar-state-persist');
				const state = JSON.parse(sessionStorage.getItem('sl-sidebar-state') || '0');
				if (!target || !state || target.dataset.hash !== state.hash) return;
				window._starlightScrollRestore = state.scroll;
				customElements.define(
					'sl-sidebar-restore',
					class SidebarRestore extends HTMLElement {
						connectedCallback() {
							try {
								const idx = parseInt(this.dataset.index || '');
								const details = this.closest('details');
								if (details && typeof state.open[idx] === 'boolean') details.open = state.open[idx];
							} catch {}
						}
					}
				);
			} catch {}
		})();
	</script>  <ul class="top-level astro-3ii7xxms"> <li class="astro-3ii7xxms"> <a href="/introduction/" class="large astro-3ii7xxms"> <span class="astro-3ii7xxms">What is Polytoken?</span>  </a> </li><li class="astro-3ii7xxms"> <details open class="astro-3ii7xxms"> <summary class="astro-3ii7xxms"> <span class="group-label astro-3ii7xxms"> <span class="large astro-3ii7xxms">Getting Started</span>  </span> <svg aria-hidden="true" class="caret astro-3ii7xxms astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1.25rem;"><path d="m14.83 11.29-4.24-4.24a1 1 0 1 0-1.42 1.41L12.71 12l-3.54 3.54a1 1 0 0 0 0 1.41 1 1 0 0 0 .71.29 1 1 0 0 0 .71-.29l4.24-4.24a1.002 1.002 0 0 0 0-1.42Z"/></svg> </summary> <sl-sidebar-restore data-index="0"></sl-sidebar-restore> <ul class="astro-3ii7xxms"> <li class="astro-3ii7xxms"> <a href="/installation/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Installation</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/installation/downloads/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Downloads</span> <span class="sl-badge default small  astro-3ii7xxms astro-avdet4wd">0.5.5</span> </a> </li><li class="astro-3ii7xxms"> <a href="/installation/updating/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Updating Polytoken</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/quick-start/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Quickstart</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/changelog/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Changelog</span>  </a> </li> </ul> </details> </li><li class="astro-3ii7xxms"> <details open class="astro-3ii7xxms"> <summary class="astro-3ii7xxms"> <span class="group-label astro-3ii7xxms"> <span class="large astro-3ii7xxms">Using Polytoken</span>  </span> <svg aria-hidden="true" class="caret astro-3ii7xxms astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1.25rem;"><path d="m14.83 11.29-4.24-4.24a1 1 0 1 0-1.42 1.41L12.71 12l-3.54 3.54a1 1 0 0 0 0 1.41 1 1 0 0 0 .71.29 1 1 0 0 0 .71-.29l4.24-4.24a1.002 1.002 0 0 0 0-1.42Z"/></svg> </summary> <sl-sidebar-restore data-index="1"></sl-sidebar-restore> <ul class="astro-3ii7xxms"> <li class="astro-3ii7xxms"> <a href="/using-polytoken/prompting-and-input/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Prompting and Input</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/using-polytoken/project-context/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Project Context</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/using-polytoken/managing-work/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Managing Work</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/using-polytoken/sessions/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Sessions</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/using-polytoken/permissions/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Permissions</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/using-polytoken/blocked-files/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Blocked Files</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/using-polytoken/permission-rules/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Permission Rules</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/using-polytoken/subagents/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Subagents</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/using-polytoken/web-search/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Web Search</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/using-polytoken/crash-reporting-and-feedback/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Crash Reporting and Feedback</span>  </a> </li> </ul> </details> </li><li class="astro-3ii7xxms"> <details open class="astro-3ii7xxms"> <summary class="astro-3ii7xxms"> <span class="group-label astro-3ii7xxms"> <span class="large astro-3ii7xxms">Harness Engineering</span>  </span> <svg aria-hidden="true" class="caret astro-3ii7xxms astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1.25rem;"><path d="m14.83 11.29-4.24-4.24a1 1 0 1 0-1.42 1.41L12.71 12l-3.54 3.54a1 1 0 0 0 0 1.41 1 1 0 0 0 .71.29 1 1 0 0 0 .71-.29l4.24-4.24a1.002 1.002 0 0 0 0-1.42Z"/></svg> </summary> <sl-sidebar-restore data-index="2"></sl-sidebar-restore> <ul class="astro-3ii7xxms"> <li class="astro-3ii7xxms"> <a href="/harness-engineering/templating/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Templating</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/harness-engineering/facets/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Facets</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/harness-engineering/subagents/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Subagents</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/harness-engineering/skills/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Skills</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/harness-engineering/hooks/" aria-current="page" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Hooks</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/harness-engineering/themes/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Themes</span>  </a> </li> </ul> </details> </li><li class="astro-3ii7xxms"> <details open class="astro-3ii7xxms"> <summary class="astro-3ii7xxms"> <span class="group-label astro-3ii7xxms"> <span class="large astro-3ii7xxms">Extending Polytoken</span>  </span> <svg aria-hidden="true" class="caret astro-3ii7xxms astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1.25rem;"><path d="m14.83 11.29-4.24-4.24a1 1 0 1 0-1.42 1.41L12.71 12l-3.54 3.54a1 1 0 0 0 0 1.41 1 1 0 0 0 .71.29 1 1 0 0 0 .71-.29l4.24-4.24a1.002 1.002 0 0 0 0-1.42Z"/></svg> </summary> <sl-sidebar-restore data-index="3"></sl-sidebar-restore> <ul class="astro-3ii7xxms"> <li class="astro-3ii7xxms"> <a href="/extending-polytoken/polytoken-vfs/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">The Polytoken VFS</span>  </a> </li> </ul> </details> </li><li class="astro-3ii7xxms"> <details open class="astro-3ii7xxms"> <summary class="astro-3ii7xxms"> <span class="group-label astro-3ii7xxms"> <span class="large astro-3ii7xxms">Reference</span>  </span> <svg aria-hidden="true" class="caret astro-3ii7xxms astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1.25rem;"><path d="m14.83 11.29-4.24-4.24a1 1 0 1 0-1.42 1.41L12.71 12l-3.54 3.54a1 1 0 0 0 0 1.41 1 1 0 0 0 .71.29 1 1 0 0 0 .71-.29l4.24-4.24a1.002 1.002 0 0 0 0-1.42Z"/></svg> </summary> <sl-sidebar-restore data-index="4"></sl-sidebar-restore> <ul class="astro-3ii7xxms"> <li class="astro-3ii7xxms"> <a href="/reference/daemon-auth/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Daemon Authentication</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/reference/cli/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">CLI Reference</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/reference/commands/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Command Reference</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/reference/configuration/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Application Configuration</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/reference/permissions-config/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Permissions Configuration</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/reference/template-reference/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Template Reference</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/reference/theme-tokens/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Theme Token Reference</span>  </a> </li><li class="astro-3ii7xxms"> <a href="/reference/tools/" class="astro-3ii7xxms"> <span class="astro-3ii7xxms">Tool Reference</span>  </a> </li> </ul> </details> </li> </ul>  <script aria-hidden="true">
		(() => {
			const scroller = document.getElementById('starlight__sidebar');
			if (!window._starlightScrollRestore || !scroller) return;
			scroller.scrollTop = window._starlightScrollRestore;
			delete window._starlightScrollRestore;
		})();
	</script> </sl-sidebar-state-persist> <div class="md:sl-hidden"> <div class="mobile-preferences sl-flex astro-wu23bvmt"> <div class="social-icons astro-wu23bvmt"> <a href="https://discord.gg/5fhv7mxEUZ" rel="me" class="sl-flex astro-wy4te6ga"><span class="sr-only astro-wy4te6ga">Discord</span><svg aria-hidden="true" class="astro-wy4te6ga astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M20.32 4.37a19.8 19.8 0 0 0-4.93-1.51 13.78 13.78 0 0 0-.64 1.28 18.27 18.27 0 0 0-5.5 0 12.64 12.64 0 0 0-.64-1.28h-.05A19.74 19.74 0 0 0 3.64 4.4 20.26 20.26 0 0 0 .11 18.09l.02.02a19.9 19.9 0 0 0 6.04 3.03l.04-.02a14.24 14.24 0 0 0 1.23-2.03.08.08 0 0 0-.05-.07 13.1 13.1 0 0 1-1.9-.92.08.08 0 0 1 .02-.1 10.2 10.2 0 0 0 .41-.31h.04a14.2 14.2 0 0 0 12.1 0l.04.01a9.63 9.63 0 0 0 .4.32.08.08 0 0 1-.03.1 12.29 12.29 0 0 1-1.9.91.08.08 0 0 0-.02.1 15.97 15.97 0 0 0 1.27 2.01h.04a19.84 19.84 0 0 0 6.03-3.05v-.03a20.12 20.12 0 0 0-3.57-13.69ZM8.02 15.33c-1.18 0-2.16-1.08-2.16-2.42 0-1.33.96-2.42 2.16-2.42 1.21 0 2.18 1.1 2.16 2.42 0 1.34-.96 2.42-2.16 2.42Zm7.97 0c-1.18 0-2.15-1.08-2.15-2.42 0-1.33.95-2.42 2.15-2.42 1.22 0 2.18 1.1 2.16 2.42 0 1.34-.94 2.42-2.16 2.42Z"/></svg></a><a href="https://bsky.app/profile/polytoken.dev" rel="me" class="sl-flex astro-wy4te6ga"><span class="sr-only astro-wy4te6ga">Bluesky</span><svg aria-hidden="true" class="astro-wy4te6ga astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M12 10.8c-1-2.1-4-6-6.8-8C2.6 1 1.6 1.3.9 1.6.1 1.9 0 3 0 3.8c0 .7.4 5.6.6 6.4C1.4 13 4.3 14 7 13.6h.4H7c-4 .6-7.4 2-2.8 7 5 5.3 6.8-1 7.8-4.2 1 3.2 2 9.3 7.7 4.3 4.3-4.3 1.2-6.5-2.7-7a9 9 0 0 1-.4-.1h.4c2.7.3 5.6-.6 6.4-3.4.2-.8.6-5.7.6-6.4 0-.7-.1-1.9-.9-2.2-.7-.3-1.7-.7-4.3 1.2-2.8 2-5.7 5.9-6.8 8"/></svg></a> </div> <starlight-theme-select>  <label style="--sl-select-width: 6.25em" class="astro-4yphtoen"> <span class="sr-only astro-4yphtoen">Select theme</span> <svg aria-hidden="true" class="icon label-icon astro-4yphtoen astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M21 14h-1V7a3 3 0 0 0-3-3H7a3 3 0 0 0-3 3v7H3a1 1 0 0 0-1 1v2a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3v-2a1 1 0 0 0-1-1ZM6 7a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v7H6V7Zm14 10a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-1h16v1Z"/></svg> <select autocomplete="off" class="astro-4yphtoen"> <option value="dark" class="astro-4yphtoen">Dark</option><option value="light" class="astro-4yphtoen">Light</option><option value="auto" selected class="astro-4yphtoen">Auto</option> </select> <svg aria-hidden="true" class="icon caret astro-4yphtoen astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1em;"><path d="M17 9.17a1 1 0 0 0-1.41 0L12 12.71 8.46 9.17a1 1 0 1 0-1.41 1.42l4.24 4.24a1.002 1.002 0 0 0 1.42 0L17 10.59a1.002 1.002 0 0 0 0-1.42Z"/></svg> </label> </starlight-theme-select>  <script>
	StarlightThemeProvider.updatePickers();
</script>   </div> </div> </div> </div> </nav> <div class="main-frame astro-vrdttmbt">  <script type="module">const a=document.getElementById("starlight__sidebar"),n=a?.querySelector("sl-sidebar-state-persist"),o="sl-sidebar-state",i=()=>{let t=[];const e=n?.dataset.hash||"";try{const s=sessionStorage.getItem(o),r=JSON.parse(s||"{}");Array.isArray(r.open)&&r.hash===e&&(t=r.open)}catch{}return{hash:e,open:t,scroll:a?.scrollTop||0}},c=t=>{try{sessionStorage.setItem(o,JSON.stringify(t))}catch{}},d=()=>c(i()),l=(t,e)=>{const s=i();s.open[e]=t,c(s)};n?.addEventListener("click",t=>{if(!(t.target instanceof Element))return;const e=t.target.closest("summary")?.closest("details");if(!e)return;const s=e.querySelector("sl-sidebar-restore"),r=parseInt(s?.dataset.index||"");isNaN(r)||l(!e.open,r)});addEventListener("visibilitychange",()=>{document.visibilityState==="hidden"&&d()});addEventListener("pageHide",d);</script> <div class="lg:sl-flex astro-67yu43on"> <aside class="right-sidebar-container print:hidden astro-67yu43on"> <div class="right-sidebar astro-67yu43on"> <div class="lg:sl-hidden astro-pb3aqygn"><mobile-starlight-toc data-min-h="2" data-max-h="3" class="astro-doynk5tl"><nav aria-labelledby="starlight__on-this-page--mobile" class="astro-doynk5tl"><details id="starlight__mobile-toc" class="astro-doynk5tl"><summary id="starlight__on-this-page--mobile" class="sl-flex astro-doynk5tl"><span class="toggle sl-flex astro-doynk5tl">On this page<svg aria-hidden="true" class="caret astro-doynk5tl astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1rem;"><path d="m14.83 11.29-4.24-4.24a1 1 0 1 0-1.42 1.41L12.71 12l-3.54 3.54a1 1 0 0 0 0 1.41 1 1 0 0 0 .71.29 1 1 0 0 0 .71-.29l4.24-4.24a1.002 1.002 0 0 0 0-1.42Z"/></svg></span><span class="display-current astro-doynk5tl"></span></summary><div class="dropdown astro-doynk5tl"><ul class="isMobile astro-gnoq344e" style="--depth: 0;"> <li class="astro-gnoq344e" style="--depth: 0;"> <a href="#_top" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Overview</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#where-hooks-live" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Where hooks live</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#writing-a-hook" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Writing a hook</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#events" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Events</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#matching" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Matching</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#handlers" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Handlers</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#what-a-handler-returns" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">What a handler returns</span> </a> <ul class="isMobile astro-gnoq344e" style="--depth: 1;"> <li class="astro-gnoq344e" style="--depth: 1;"> <a href="#blocking-events" class="astro-gnoq344e" style="--depth: 1;"> <span class="astro-gnoq344e" style="--depth: 1;">Blocking events</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 1;"> <a href="#fire-and-forget-events" class="astro-gnoq344e" style="--depth: 1;"> <span class="astro-gnoq344e" style="--depth: 1;">Fire-and-forget events</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 1;"> <a href="#reporting-an-error" class="astro-gnoq344e" style="--depth: 1;"> <span class="astro-gnoq344e" style="--depth: 1;">Reporting an error</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 1;"> <a href="#exit-code-shorthand" class="astro-gnoq344e" style="--depth: 1;"> <span class="astro-gnoq344e" style="--depth: 1;">Exit-code shorthand</span> </a>  </li> </ul> </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#turning-off-an-inherited-hook" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Turning off an inherited hook</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#a-small-hook" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">A small hook</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#loading-changes" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Loading changes</span> </a>  </li> </ul></div></details></nav></mobile-starlight-toc><script type="module" src="/_astro/MobileTableOfContents.astro_astro_type_script_index_0_lang.hwBsy0Mo.js"></script></div><div class="right-sidebar-panel sl-hidden lg:sl-block astro-pb3aqygn"><div class="sl-container astro-pb3aqygn"><starlight-toc data-min-h="2" data-max-h="3"><nav aria-labelledby="starlight__on-this-page"><h2 id="starlight__on-this-page">On this page</h2><ul class="astro-gnoq344e" style="--depth: 0;"> <li class="astro-gnoq344e" style="--depth: 0;"> <a href="#_top" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Overview</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#where-hooks-live" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Where hooks live</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#writing-a-hook" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Writing a hook</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#events" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Events</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#matching" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Matching</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#handlers" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Handlers</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#what-a-handler-returns" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">What a handler returns</span> </a> <ul class="astro-gnoq344e" style="--depth: 1;"> <li class="astro-gnoq344e" style="--depth: 1;"> <a href="#blocking-events" class="astro-gnoq344e" style="--depth: 1;"> <span class="astro-gnoq344e" style="--depth: 1;">Blocking events</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 1;"> <a href="#fire-and-forget-events" class="astro-gnoq344e" style="--depth: 1;"> <span class="astro-gnoq344e" style="--depth: 1;">Fire-and-forget events</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 1;"> <a href="#reporting-an-error" class="astro-gnoq344e" style="--depth: 1;"> <span class="astro-gnoq344e" style="--depth: 1;">Reporting an error</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 1;"> <a href="#exit-code-shorthand" class="astro-gnoq344e" style="--depth: 1;"> <span class="astro-gnoq344e" style="--depth: 1;">Exit-code shorthand</span> </a>  </li> </ul> </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#turning-off-an-inherited-hook" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Turning off an inherited hook</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#a-small-hook" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">A small hook</span> </a>  </li><li class="astro-gnoq344e" style="--depth: 0;"> <a href="#loading-changes" class="astro-gnoq344e" style="--depth: 0;"> <span class="astro-gnoq344e" style="--depth: 0;">Loading changes</span> </a>  </li> </ul></nav></starlight-toc><script type="module" src="/_astro/TableOfContents.astro_astro_type_script_index_0_lang.FuRcXuRY.js"></script></div></div> </div> </aside> <div class="main-pane astro-67yu43on">  <main data-pagefind-body class="astro-bguv2lll" lang="en" dir="ltr">    <div class="content-panel astro-7nkwcw3z"> <div class="sl-container astro-7nkwcw3z"> <h1 id="_top" class="astro-j6tvhyss">Hooks</h1> </div> </div> <div class="content-panel astro-7nkwcw3z"> <div class="sl-container astro-7nkwcw3z"> <div class="sl-markdown-content"> <p>A hook runs your code at a fixed point in the agent loop, such as before a tool
runs or when a session starts. Polytoken calls the hook, hands it a description of
what is about to happen, and reads back a decision. A hook can observe the event,
add context the model will see, or stop the action outright.</p>
<div class="sl-heading-wrapper level-h2"><h2 id="where-hooks-live">Where hooks live</h2><a class="sl-anchor-link" href="#where-hooks-live"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Where hooks live”</span></a></div>
<p>You define hooks in a <code dir="auto">hooks.json</code> file. Polytoken reads two of them:</p>
<ul>
<li><strong>Global</strong>, at <code dir="auto">hooks.json</code> in your Polytoken config directory, for hooks you
want in every project.</li>
<li><strong>Project</strong>, at <code dir="auto">.polytoken/hooks.json</code> in your project, for hooks specific to
that project.</li>
</ul>
<p>Each file is a JSON array of hook entries. Polytoken loads the global entries
first, then appends the project entries, and runs them in that order for any
event they match.</p>
<div class="sl-heading-wrapper level-h2"><h2 id="writing-a-hook">Writing a hook</h2><a class="sl-anchor-link" href="#writing-a-hook"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Writing a hook”</span></a></div>
<p>A hook entry has four fields:</p>
<div class="expressive-code"><link rel="stylesheet" href="/_astro/ec.v4551.css"><script type="module" src="/_astro/ec.0vx5m.js"></script><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#7FDBCA;--1:#096E72">"name"</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#C789D6;--1:#7C5686">log-edits</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#7FDBCA;--1:#096E72">"event"</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#C789D6;--1:#7C5686">post_tool_use</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#7FDBCA;--1:#096E72">"matcher"</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#C789D6;--1:#7C5686">file_edit_*</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#7FDBCA;--1:#096E72">"handler"</span><span style="--0:#D6DEEB;--1:#403F53">: { </span><span style="--0:#7FDBCA;--1:#096E72">"bash"</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#C789D6;--1:#7C5686">cat >> /tmp/polytoken-edits.log</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53"> }</span></div></div><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="{  &#x22;name&#x22;: &#x22;log-edits&#x22;,  &#x22;event&#x22;: &#x22;post_tool_use&#x22;,  &#x22;matcher&#x22;: &#x22;file_edit_*&#x22;,  &#x22;handler&#x22;: { &#x22;bash&#x22;: &#x22;cat >> /tmp/polytoken-edits.log&#x22; }}"><div></div></button></div></figure></div>



































<table><thead><tr><th>Field</th><th>Type</th><th>Required</th><th>Meaning</th></tr></thead><tbody><tr><td><code dir="auto">name</code></td><td>string</td><td>yes</td><td>A string identifying the hook. Used in logs and in the negation syntax below.</td></tr><tr><td><code dir="auto">event</code></td><td>string</td><td>yes</td><td>The point in the loop that fires this hook. One of the names in <a href="#events">Events</a>.</td></tr><tr><td><code dir="auto">matcher</code></td><td>string</td><td>no</td><td>A glob that narrows which instances of the event fire the hook. Omit it to fire on every instance. See <a href="#matching">Matching</a>.</td></tr><tr><td><code dir="auto">handler</code></td><td>object</td><td>yes</td><td>The code to run. See <a href="#handlers">Handlers</a>.</td></tr></tbody></table>
<p>Polytoken validates the file at load time. It rejects an unknown <code dir="auto">event</code> name,
an unparseable <code dir="auto">matcher</code> glob, or an unknown handler key as a load error. A
malformed hook fails loudly rather than silently never firing.</p>
<div class="sl-heading-wrapper level-h2"><h2 id="events">Events</h2><a class="sl-anchor-link" href="#events"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Events”</span></a></div>
<p>An event is a point in the agent loop. Each event passes its handler a different
set of fields and reads back a different decision.</p>
<p>Read the <strong>Waits</strong> column first. Polytoken waits for a blocking event’s handler
and acts on what it returns, so a blocking hook can add context or stop the
action. A fire-and-forget hook runs in the background and Polytoken discards what
it returns, so use one for side effects such as logging, not for changing what
Polytoken does next.</p>
















































































<table><thead><tr><th>Event</th><th>Waits</th><th>Fires</th></tr></thead><tbody><tr><td><code dir="auto">session_start</code></td><td>yes</td><td>When a session begins.</td></tr><tr><td><code dir="auto">pre_user_prompt</code></td><td>yes</td><td>Before Polytoken records a prompt you submit.</td></tr><tr><td><code dir="auto">pre_model_turn</code></td><td>yes</td><td>Before Polytoken calls the model for a turn.</td></tr><tr><td><code dir="auto">post_model_turn</code></td><td>no</td><td>After the model finishes a turn.</td></tr><tr><td><code dir="auto">pre_tool_use</code></td><td>yes</td><td>Before a tool runs.</td></tr><tr><td><code dir="auto">post_tool_use</code></td><td>no</td><td>After a tool succeeds.</td></tr><tr><td><code dir="auto">post_tool_use_failure</code></td><td>no</td><td>After a tool fails.</td></tr><tr><td><code dir="auto">stop</code></td><td>yes</td><td>When the model would finish and Polytoken would hand the turn back to you.</td></tr><tr><td><code dir="auto">pre_compaction</code></td><td>yes</td><td>Before Polytoken compacts the session.</td></tr><tr><td><code dir="auto">post_compaction</code></td><td>yes</td><td>After Polytoken compacts the session.</td></tr><tr><td><code dir="auto">notification</code></td><td>yes</td><td>When Polytoken would raise a notification.</td></tr><tr><td><code dir="auto">facet_switch</code></td><td>no</td><td>After the active facet changes.</td></tr><tr><td><code dir="auto">subagent_start</code></td><td>no</td><td>After a subagent starts.</td></tr><tr><td><code dir="auto">subagent_stop</code></td><td>no</td><td>After a subagent finishes.</td></tr></tbody></table>
<p>A handler reads the event’s details from JSON on its standard input. Every event
passes at least its own name and the matcher subject. Tool events add the tool
name and its input. Subagent events add the subagent type. Polytoken also sets
<code dir="auto">POLYTOKEN_*</code> environment variables for the handler: <code dir="auto">POLYTOKEN_HOOK_EVENT</code>,
<code dir="auto">POLYTOKEN_HANDLER_NAME</code>, <code dir="auto">POLYTOKEN_HOOK_MATCHER_SUBJECT</code>,
<code dir="auto">POLYTOKEN_NON_INTERACTIVE</code>, and <code dir="auto">POLYTOKEN_GOAL_ACTIVE</code> on every hook, and
<code dir="auto">POLYTOKEN_SESSION_ID</code>, <code dir="auto">POLYTOKEN_PROJECT_DIR</code>, <code dir="auto">POLYTOKEN_PROJECT_PATH</code>,
<code dir="auto">POLYTOKEN_FACET_NAME</code>, and <code dir="auto">POLYTOKEN_MODEL_NAME</code> when the session, project,
facet, and model are known. <code dir="auto">POLYTOKEN_GOAL_ACTIVE</code> is <code dir="auto">true</code> or <code dir="auto">false</code>
depending on whether a saved-session goal is running. <code dir="auto">POLYTOKEN_FACET_NAME</code> is
the active facet name (for example, <code dir="auto">plan</code> or <code dir="auto">execute</code>), and
<code dir="auto">POLYTOKEN_MODEL_NAME</code> is the active model’s config-key name (for example,
<code dir="auto">claude-opus-4-6</code>).</p>
<div class="sl-heading-wrapper level-h2"><h2 id="matching">Matching</h2><a class="sl-anchor-link" href="#matching"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Matching”</span></a></div>
<p>A <code dir="auto">matcher</code> is a glob. When a hook has one, Polytoken fires the hook only when
the glob matches the event’s subject. The subject depends on the event:</p>
<ul>
<li>For <code dir="auto">pre_tool_use</code>, <code dir="auto">post_tool_use</code>, and <code dir="auto">post_tool_use_failure</code>, the subject
is the tool name, so <code dir="auto">"matcher": "file_read"</code> fires only for the <code dir="auto">file_read</code>
tool and <code dir="auto">"matcher": "file_edit_*"</code> fires for every edit tool whose name starts
with <code dir="auto">file_edit_</code>.</li>
<li>For <code dir="auto">subagent_start</code> and <code dir="auto">subagent_stop</code>, the subject is the subagent type.</li>
<li>For every other event, the subject is the event name itself, so a <code dir="auto">matcher</code> on
those events is rarely useful: leave it off and the hook fires every time.</li>
</ul>
<p>The glob syntax is the usual shell style: <code dir="auto">*</code> matches within a segment, <code dir="auto">**</code>
matches across segments, <code dir="auto">?</code> matches one character, and <code dir="auto">[a-z]</code> matches a range.</p>
<div class="sl-heading-wrapper level-h2"><h2 id="handlers">Handlers</h2><a class="sl-anchor-link" href="#handlers"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Handlers”</span></a></div>
<p>The <code dir="auto">handler</code> object names what Polytoken runs. It has a <code dir="auto">bash</code> key whose value is
a Bash script:</p>
<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">{ </span><span style="--0:#7FDBCA;--1:#096E72">"bash"</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#C789D6;--1:#7C5686">jq -r .tool_name >> /tmp/tools-used.log</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53"> }</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="{ &#x22;bash&#x22;: &#x22;jq -r .tool_name >> /tmp/tools-used.log&#x22; }"><div></div></button></div></figure></div>
<p>Polytoken runs the script, writes the event JSON to its standard input, and sets
the <code dir="auto">POLYTOKEN_*</code> environment variables. The script reports its decision on
standard output or through its exit code, as the sections below describe.</p>
<p>A handler has a short deadline to finish, so a hung handler cannot stall the agent
loop. Polytoken treats a handler that runs past the deadline as an error for that
event.</p>
<div class="sl-heading-wrapper level-h2"><h2 id="what-a-handler-returns">What a handler returns</h2><a class="sl-anchor-link" href="#what-a-handler-returns"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “What a handler returns”</span></a></div>
<p>A handler reports its decision as a single JSON object on standard output, tagged
by an <code dir="auto">outcome</code> field. Each event defines its own set of outcomes, named for what
that event does, so the outcome you return depends on the event the hook is
attached to. An outcome carries only the fields that event reads; an unknown field
is an error.</p>
<div class="sl-heading-wrapper level-h3"><h3 id="blocking-events">Blocking events</h3><a class="sl-anchor-link" href="#blocking-events"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Blocking events”</span></a></div>
<p>A blocking event reads its handler’s outcome and acts on it. Every blocking event
accepts a proceed outcome; most also accept a stop outcome, and two accept a
<code dir="auto">suppress</code> outcome that holds the action back quietly:</p>


















































<table><thead><tr><th>Event</th><th>Outcomes</th><th>Fields you can set</th></tr></thead><tbody><tr><td><code dir="auto">pre_tool_use</code></td><td><code dir="auto">allow</code>, <code dir="auto">deny</code></td><td><code dir="auto">deny</code>: <code dir="auto">reason</code>.</td></tr><tr><td><code dir="auto">pre_user_prompt</code></td><td><code dir="auto">accept</code>, <code dir="auto">reject</code></td><td><code dir="auto">accept</code>: <code dir="auto">additional_context</code>. <code dir="auto">reject</code>: <code dir="auto">reason</code>.</td></tr><tr><td><code dir="auto">pre_model_turn</code></td><td><code dir="auto">proceed</code>, <code dir="auto">retry</code></td><td><code dir="auto">proceed</code>: <code dir="auto">additional_context</code>. <code dir="auto">retry</code>: <code dir="auto">reason</code>.</td></tr><tr><td><code dir="auto">stop</code></td><td><code dir="auto">stop</code>, <code dir="auto">continue</code></td><td><code dir="auto">continue</code>: <code dir="auto">reason</code>.</td></tr><tr><td><code dir="auto">pre_compaction</code></td><td><code dir="auto">allow</code>, <code dir="auto">cancel</code>, <code dir="auto">suppress</code></td><td><code dir="auto">allow</code>: <code dir="auto">prepend_to_prompt</code>. <code dir="auto">cancel</code>, <code dir="auto">suppress</code>: <code dir="auto">reason</code>.</td></tr><tr><td><code dir="auto">session_start</code></td><td><code dir="auto">allow</code></td><td><code dir="auto">allow</code>: <code dir="auto">additional_context</code>.</td></tr><tr><td><code dir="auto">post_compaction</code></td><td><code dir="auto">allow</code></td><td><code dir="auto">allow</code>: <code dir="auto">append_to_output</code>.</td></tr><tr><td><code dir="auto">notification</code></td><td><code dir="auto">allow</code>, <code dir="auto">suppress</code></td><td><code dir="auto">suppress</code>: <code dir="auto">reason</code>.</td></tr></tbody></table>
<p>The stop outcome does what the event names. <code dir="auto">deny</code> stops a tool call. <code dir="auto">reject</code>
turns a prompt away. <code dir="auto">retry</code> sends the model turn back with the reason injected.
<code dir="auto">continue</code> keeps the loop going instead of letting the model hand the turn back to
you. <code dir="auto">cancel</code> stops the compaction. <code dir="auto">suppress</code> holds the action back quietly: a
<code dir="auto">notification</code> hook uses it to drop a notification, and a <code dir="auto">pre_compaction</code> hook uses
it to skip a compaction. Its <code dir="auto">reason</code> is optional.</p>
<p><code dir="auto">session_start</code> and <code dir="auto">post_compaction</code> accept only <code dir="auto">allow</code>: their action has already
happened, so a handler can add context but cannot stop it.</p>
<p>The <code dir="auto">additional_context</code> an <code dir="auto">allow</code> or <code dir="auto">accept</code> adds becomes a system-reminder the
model sees. <code dir="auto">prepend_to_prompt</code> and <code dir="auto">append_to_output</code> add text before and after
the compaction summary. The <code dir="auto">deny</code>, <code dir="auto">reject</code>, <code dir="auto">retry</code>, and <code dir="auto">continue</code> outcomes also
accept <code dir="auto">stdout</code> and <code dir="auto">stderr</code> fields alongside <code dir="auto">reason</code>, which capture the output of
a script that reports its decision through an exit code rather than JSON.</p>
<div class="sl-heading-wrapper level-h3"><h3 id="fire-and-forget-events">Fire-and-forget events</h3><a class="sl-anchor-link" href="#fire-and-forget-events"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Fire-and-forget events”</span></a></div>
<p><code dir="auto">post_model_turn</code>, <code dir="auto">post_tool_use</code>, <code dir="auto">post_tool_use_failure</code>, <code dir="auto">facet_switch</code>,
<code dir="auto">subagent_start</code>, and <code dir="auto">subagent_stop</code> run in the background, and Polytoken discards
what they return. A handler for one of these events returns <code dir="auto">acknowledged</code> when the
script succeeds; the side effect the script performs is the point of the hook. A
script that exits with an error reports <code dir="auto">error</code>, which Polytoken logs.</p>
<div class="sl-heading-wrapper level-h3"><h3 id="reporting-an-error">Reporting an error</h3><a class="sl-anchor-link" href="#reporting-an-error"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Reporting an error”</span></a></div>
<p>Any handler can return <code dir="auto">{ "outcome": "error", "message": "..." }</code> to say it could
not decide. Polytoken records the error and does not read it as success. On a
blocking event that gates an action, that error stops the action: an error on
<code dir="auto">pre_tool_use</code>, <code dir="auto">pre_model_turn</code>, <code dir="auto">stop</code>, or <code dir="auto">pre_compaction</code> blocks the tool call,
the turn, the handback, or the compaction, on the principle that a hook that cannot
decide should not let a guarded action proceed. Three blocking events instead fail
open and let their action proceed on an error: <code dir="auto">pre_user_prompt</code>, <code dir="auto">notification</code>,
and <code dir="auto">post_compaction</code>. A fire-and-forget event has no decision to fail, so an error
from one of its handlers is logged and nothing else changes.</p>
<div class="sl-heading-wrapper level-h3"><h3 id="exit-code-shorthand">Exit-code shorthand</h3><a class="sl-anchor-link" href="#exit-code-shorthand"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Exit-code shorthand”</span></a></div>
<p>A <code dir="auto">bash</code> handler can report its decision through its exit code, which is
convenient for a one-line script:</p>
<ul>
<li>Exit <code dir="auto">0</code> with no output is the event’s proceed outcome.</li>
<li>Exit <code dir="auto">2</code> is the event’s stop outcome on an event that has one, and Polytoken
captures what the script printed so the model sees it. On an event with no stop
outcome, exit <code dir="auto">2</code> is an error.</li>
<li>Any other non-zero exit is an error, with the script’s standard error in the
message.</li>
</ul>
<div class="sl-heading-wrapper level-h2"><h2 id="turning-off-an-inherited-hook">Turning off an inherited hook</h2><a class="sl-anchor-link" href="#turning-off-an-inherited-hook"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Turning off an inherited hook”</span></a></div>
<p>A project file can switch off a global hook by name. Add a string entry of the
hook’s name prefixed with <code dir="auto">!</code>:</p>
<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">[</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#ECC48D;--1:#984E4D">!log-edits</span><span style="--0:#D9F5DD;--1:#111111">"</span></div></div><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="[  &#x22;!log-edits&#x22;]"><div></div></button></div></figure></div>
<p>Polytoken drops the global hook named <code dir="auto">log-edits</code> for this project. The name must
match an existing global hook; otherwise Polytoken rejects the file.</p>
<div class="sl-heading-wrapper level-h2"><h2 id="a-small-hook">A small hook</h2><a class="sl-anchor-link" href="#a-small-hook"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “A small hook”</span></a></div>
<p>A project hook in <code dir="auto">.polytoken/hooks.json</code> that blocks edits to a locked file:</p>
<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">[</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">  </span></span><span style="--0:#D6DEEB;--1:#403F53">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#7FDBCA;--1:#096E72">"name"</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#C789D6;--1:#7C5686">protect-generated-reference</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#7FDBCA;--1:#096E72">"event"</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#C789D6;--1:#7C5686">pre_tool_use</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#7FDBCA;--1:#096E72">"matcher"</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#C789D6;--1:#7C5686">file_edit_search_replace</span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#D6DEEB;--1:#403F53">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#7FDBCA;--1:#096E72">"handler"</span><span style="--0:#D6DEEB;--1:#403F53">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#7FDBCA;--1:#096E72">"bash"</span><span style="--0:#D6DEEB;--1:#403F53">: </span><span style="--0:#D9F5DD;--1:#111111">"</span><span style="--0:#C789D6;--1:#7C5686">test </span><span style="--0:#F78C6C;--1:#AA0982">\"</span><span style="--0:#C789D6;--1:#7C5686">$(jq -r '.input.path // empty')</span><span style="--0:#F78C6C;--1:#AA0982">\"</span><span style="--0:#C789D6;--1:#7C5686"> = docs/reference/generated.md &#x26;&#x26; { echo 'docs/reference/generated.md is generated; do not edit it by hand.'; exit 2; }; exit 0</span><span style="--0:#D9F5DD;--1:#111111">"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">    </span></span><span style="--0:#D6DEEB;--1:#403F53">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#D6DEEB;--1:#403F53">  </span></span><span style="--0:#D6DEEB;--1:#403F53">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#D6DEEB;--1:#403F53">]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button title="Copy to clipboard" data-copied="Copied!" data-code="[  {    &#x22;name&#x22;: &#x22;protect-generated-reference&#x22;,    &#x22;event&#x22;: &#x22;pre_tool_use&#x22;,    &#x22;matcher&#x22;: &#x22;file_edit_search_replace&#x22;,    &#x22;handler&#x22;: {      &#x22;bash&#x22;: &#x22;test \&#x22;$(jq -r &#x27;.input.path // empty&#x27;)\&#x22; = docs/reference/generated.md &#x26;&#x26; { echo &#x27;docs/reference/generated.md is generated; do not edit it by hand.&#x27;; exit 2; }; exit 0&#x22;    }  }]"><div></div></button></div></figure></div>
<p>The hook fires before the <code dir="auto">file_edit_search_replace</code> tool runs. The script reads
the event JSON from standard input, checks the target path, and exits <code dir="auto">2</code> to deny
the call with a reason when the path is the locked file. For any other path it
exits <code dir="auto">0</code> and the edit proceeds.</p>
<div class="sl-heading-wrapper level-h2"><h2 id="loading-changes">Loading changes</h2><a class="sl-anchor-link" href="#loading-changes"><span aria-hidden="true" class="sl-anchor-icon"><svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentcolor" d="m12.11 15.39-3.88 3.88a2.52 2.52 0 0 1-3.5 0 2.47 2.47 0 0 1 0-3.5l3.88-3.88a1 1 0 0 0-1.42-1.42l-3.88 3.89a4.48 4.48 0 0 0 6.33 6.33l3.89-3.88a1 1 0 1 0-1.42-1.42Zm8.58-12.08a4.49 4.49 0 0 0-6.33 0l-3.89 3.88a1 1 0 0 0 1.42 1.42l3.88-3.88a2.52 2.52 0 0 1 3.5 0 2.47 2.47 0 0 1 0 3.5l-3.88 3.88a1 1 0 1 0 1.42 1.42l3.88-3.89a4.49 4.49 0 0 0 0-6.33ZM8.83 15.17a1 1 0 0 0 1.1.22 1 1 0 0 0 .32-.22l4.92-4.92a1 1 0 0 0-1.42-1.42l-4.92 4.92a1 1 0 0 0 0 1.42Z"></path></svg></span><span class="sr-only" data-pagefind-ignore="">Section titled “Loading changes”</span></a></div>
<p>Polytoken loads hooks at startup and when you reload its configuration; an edit
to <code dir="auto">hooks.json</code> takes effect only on the next reload.</p> </div> <footer class="sl-flex astro-3yyafb3n"> <div class="meta sl-flex astro-3yyafb3n">   </div> <div class="pagination-links print:hidden astro-u2l5gyhi" dir="ltr"> <a href="/harness-engineering/skills/" rel="prev" class="astro-u2l5gyhi"> <svg aria-hidden="true" class="astro-u2l5gyhi astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1.5rem;"><path d="M17 11H9.41l3.3-3.29a1.004 1.004 0 1 0-1.42-1.42l-5 5a1 1 0 0 0-.21.33 1 1 0 0 0 0 .76 1 1 0 0 0 .21.33l5 5a1.002 1.002 0 0 0 1.639-.325 1 1 0 0 0-.219-1.095L9.41 13H17a1 1 0 0 0 0-2Z"/></svg> <span class="astro-u2l5gyhi"> Previous <br class="astro-u2l5gyhi"> <span class="link-title astro-u2l5gyhi">Skills</span> </span> </a> <a href="/harness-engineering/themes/" rel="next" class="astro-u2l5gyhi"> <svg aria-hidden="true" class="astro-u2l5gyhi astro-c6vsoqas" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1.5rem;"><path d="M17.92 11.62a1.001 1.001 0 0 0-.21-.33l-5-5a1.003 1.003 0 1 0-1.42 1.42l3.3 3.29H7a1 1 0 0 0 0 2h7.59l-3.3 3.29a1.002 1.002 0 0 0 .325 1.639 1 1 0 0 0 1.095-.219l5-5a1 1 0 0 0 .21-.33 1 1 0 0 0 0-.76Z"/></svg> <span class="astro-u2l5gyhi"> Next <br class="astro-u2l5gyhi"> <span class="link-title astro-u2l5gyhi">Themes</span> </span> </a> </div>  </footer> </div> </div>  </main> </div> </div> </div> </div> </body></html>