const IS_PRODUCTION = process.env.NODE_ENV === 'production'

module.exports = {
    outputDir: 'dist',
    assetsDir: 'static',
    baseUrl: IS_PRODUCTION
    // For Production, replace Static Base Url with Static Server / CDN
    // And then point your CDN to yourdomain.com/static
    // Use Whitenoise to serve assets at /static
    // and have your cdn cache and distribute
      ? '/' // eg. www.cdn123.com/
      : '/',
    devServer: {
      proxy: {
        '/api*': {
          // Forward frontend dev server request for /api to django devserver
          target: 'http://localhost:8000/',
        }
      }
    }
  }
