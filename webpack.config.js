const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');

module.exports = (env, argv) => {
  if(!argv.name)
    throw "Set Folder Name: npm run less -- --name={name}";

  function abspath(relpath) {
    return path.resolve(__dirname, './'+argv.name+'/'+relpath);
  }

  return {
    mode: "production",
    entry: {
      mobile: abspath('custom_mobile.less'),
      desktop: abspath('custom_desktop.less')
    },
    output: {
      path: abspath('dist'),
      filename: "no-use-[name].js"
    },
    module: {
      rules: [{
        test: /\.less$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          "less-loader"
        ]
      }]
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: '[name]-min.css'
      })
    ],
    optimization: {
      minimizer: [new OptimizeCSSAssetsPlugin({})]
    }
  }
};
