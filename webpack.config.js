const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');

module.exports = {
	mode: "production",
	entry: "./my.less",
	output: {
		path: path.resolve(__dirname, './dist'),
		filename: "no-use.js"
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
};
