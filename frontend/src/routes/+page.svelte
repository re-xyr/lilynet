<script lang="ts">
const { data } = $props()
</script>

<div class="prose prose-neutral">
  <p>
    <strong>Lilynet</strong> is <a href="https://dayli.ly">daylily</a>'s personal experimental
    network.
  </p>

  <p>
    Lilynet is <a href="https://bgp.tools/as/401736">AS401736</a> on the clearnet (registered with
    ARIN) and <a href="https://explorer.dn42.dev/#/AS4242421919">AS4242421919</a> on dn42. AS401736 is
    controlled by Project Daylily, the sole proprietorship of daylily.
  </p>

  <p>Currently, we originate the following prefixes:</p>

  <ul>
    <li><code>2620:d7:6000::/48</code> on the clearnet.</li>
    <li><code>fd11:4514:1919::/48</code> on dn42.</li>
    <li><code>172.21.89.64/27</code> on dn42.</li>
  </ul>

  <p>Our clearnet upstream is The Constant Company / Vultr (AS20473).</p>

  <p>We currently provide the following services on Lilynet:</p>

  <ul>
    <li>Authoritative DNS of <code>daylily.network</code>.</li>
    <li>Authoritative rDNS of our clearnet prefixes.</li>
    <li>IPv6 and dn42 tunneling for our affiliates.</li>
    <li>Routing to our servers under our owned prefixes.</li>
    <li>
      dn42 peering; refer to the <a href="https://dayli.ly/dn42">dn42 peering policy</a> for more information.
    </li>
  </ul>

  <hr />

  <p class="font-italic">
    You are currently accessing this page from IP <code>{data.meta.clientIp}</code> via
    <code>{data.meta.host}</code>.
    {#if data.meta.anycast}This is an anycast hostname{/if}
    {#if !data.meta.anycast}This is a unicast hostname{/if}
    and is served by Lilynet edge node <code>{data.meta.node}</code>.
  </p>
</div>
