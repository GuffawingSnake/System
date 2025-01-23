module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          '^/api': '/api'
        },
        onProxyReq(proxyReq, req) {
          console.log('代理请求:', req.method, req.url, '到', proxyReq.path)
        },
        onProxyRes(proxyRes, req) {
          console.log('代理响应:', proxyRes.statusCode, req.url)
        },
        onError(err, req, res) {
          console.error('代理错误:', err)
        }
      }
    },
    host: 'localhost',
    port: 8080,
    https: false
  }
}
