<script lang="ts">
import type { LayoutProps } from './$types'

const { children }: LayoutProps = $props()
</script>

<div class="prose prose-stone">
  {@render children()}
</div>
