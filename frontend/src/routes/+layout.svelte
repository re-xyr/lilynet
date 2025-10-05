<script lang="ts">
import '../app.css'
import '@fontsource-variable/ubuntu-sans'
import '@fontsource-variable/ubuntu-sans/wght-italic.css'
import '@fontsource-variable/ubuntu-sans-mono'
import '@fontsource-variable/ubuntu-sans-mono/wght-italic.css'

import { page } from '$app/state'
import type { LayoutProps } from './$types'
import { VERSION } from '@sveltejs/kit'

let { children, data }: LayoutProps = $props()

const displayTitle = $derived(
  page.url.pathname === '/' ? 'Lilynet' : `Lilynet - ${page.url.pathname}`,
)
const description = "Lilynet (AS401736, AS4242421919) is daylily's personal experimental network."
</script>

<svelte:head>
  <title>{displayTitle}</title>

  <meta name="author" content="Project Daylily" />
  <meta name="generator" content="SvelteKit {VERSION}" />
  <meta name="description" content={description} />

  <meta property="og:title" content={displayTitle} />
  <meta property="og:type" content="website" />
  <meta property="og:url" content={page.url.toString()} />
  <meta property="og:description" content={description} />
  <meta property="og:site_name" content="dayli.ly" />
</svelte:head>

<div class="flex min-h-dvh flex-col items-center bg-stone-100 px-4 py-12 text-stone-800">
  <div class="flex w-full max-w-xl grow flex-col gap-12">
    <header class="flex flex-row items-center gap-2">
      <h1 class="text-xl font-bold">
        <a href="/" class="flex flex-row items-center gap-2">
          <img src="/favicon.svg" alt="Lilynet Logo" class="size-6" />
          Lilynet
        </a>
      </h1>
      <div class="grow text-stone-600">{page.url.pathname}</div>
      <div class="text-sm text-stone-600">
        {data.meta.node}
        {#if data.meta.anycast}anycast{/if}
      </div>
    </header>

    <main class="grow">
      {@render children()}
    </main>

    <footer class="flex flex-row items-center text-sm text-stone-500">
      <p class="grow">
        Powered by <a
          href="https://svelte.dev"
          target="_blank"
          rel="noopener noreferrer"
          class="underline hover:no-underline"
        >
          SvelteKit
        </a>
      </p>
      <p>
        2025 &copy; <a
          href="https://dayli.ly"
          target="_blank"
          rel="noopener noreferrer"
          class="underline hover:no-underline">Project Daylily</a
        >
      </p>
    </footer>
  </div>
</div>
