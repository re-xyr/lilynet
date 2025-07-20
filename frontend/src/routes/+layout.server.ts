export const load = ({ request }) => {
  return {
    meta: {
      node: request.headers.get('x-lilynet-node') || 'unknown',
      host: request.headers.get('x-forwarded-host') || 'unknown',
      anycast: request.headers.get('x-lilynet-anycast') ? true : false,
      clientIp: request.headers.get('x-forwarded-for') || 'unknown',
    },
  }
}
