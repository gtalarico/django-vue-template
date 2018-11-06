// Vue-cli3 customized configuration
// const IS_PRODUCTION = process.env.NODE_ENV === 'production'

const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin')

module.exports = {
    outputDir: 'dist',
    assetsDir: 'static',
    // baseUrl: IS_PRODUCTION
    // ? 'http://cdn123.com'
    // : '/',
    // For Production, replace set baseUrl to CDN
    // And set the CDN origin to `yourdomain.com/static`
    // Whitenoise will serve once to CDN which will then cache
    // and distribute
    configureWebpack: {
      plugins: [
      new VuetifyLoaderPlugin()
      ]
    },

    devServer: {
      proxy: {
        '/api*': {
          // Forward frontend dev server request for /api to django dev server
          target: 'http://localhost:8000/',
        }
      }
    }
  }
