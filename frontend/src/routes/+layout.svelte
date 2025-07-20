<script lang="ts">
import '../app.css'
import '@fontsource-variable/ubuntu-sans'
import '@fontsource-variable/ubuntu-sans/wght-italic.css'
import '@fontsource-variable/ubuntu-sans-mono'
import '@fontsource-variable/ubuntu-sans-mono/wght-italic.css'

import { page } from '$app/state'
import type { LayoutProps } from './$types'

let { children, data }: LayoutProps = $props()
</script>

<div class="flex min-h-dvh flex-col items-center px-4 py-12">
  <div class="flex w-full max-w-xl grow flex-col gap-12">
    <header class="flex flex-row items-center gap-2">
      <h1 class="text-xl font-bold">
        <a href="/" class="flex flex-row items-center gap-2">
          <img src="/favicon.svg" alt="Lilynet Logo" class="size-6" />
          Lilynet
        </a>
      </h1>
      <div class="grow text-neutral-600">{page.url.pathname}</div>
      <div class="text-sm text-neutral-600">
        {data.meta.node}
        {#if data.meta.anycast}anycast{/if}
      </div>
    </header>

    <main class="grow">
      {@render children()}
    </main>

    <footer class="flex flex-row items-center text-sm text-gray-500">
      <p class="grow">
        Powered by <a
          href="https://svelte.dev"
          target="_blank"
          rel="noopener noreferrer"
          class="underline"
        >
          SvelteKit
        </a>
      </p>
      <p>
        2025 &copy; <a
          href="https://dayli.ly"
          target="_blank"
          rel="noopener noreferrer"
          class="underline">Project Daylily</a
        >
      </p>
    </footer>
  </div>
</div>
