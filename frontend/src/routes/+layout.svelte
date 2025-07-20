<script lang="ts">
import '../app.css'
import { page } from '$app/state'
import type { LayoutProps } from './$types'

let { children, data }: LayoutProps = $props()
</script>

<div class="flex min-h-dvh flex-col items-center px-4 py-8">
  <div class="flex w-full max-w-xl grow flex-col gap-8">
    <header class="flex flex-row items-center gap-2">
      <h1 class="text-xl font-semibold">Lilynet</h1>
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
      <p class="grow">Powered by SvelteKit</p>
      <p>2025 &copy; Project Daylily</p>
    </footer>
  </div>
</div>
