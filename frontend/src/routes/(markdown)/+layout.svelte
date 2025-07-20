<script lang="ts">
import type { LayoutProps } from './$types'

const { children }: LayoutProps = $props()
</script>

<div
  class="prose prose-neutral prose-a:font-normal prose-a:text-cyan-900 prose-a:decoration-1 prose-a:hover:text-cyan-700 prose-a:transition-colors prose-code:font-medium"
>
  {@render children()}
</div>
