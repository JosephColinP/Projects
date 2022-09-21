const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const CopyPlugin = require("copy-webpack-plugin");
const Dotenv = require('dotenv-webpack');


module.exports ={
  entry: {
    main: path.resolve(__dirname, "src/js/index.js")
  }, output: {
    path: path.resolve(__dirname, "dist"),
    filename: "js/[name].[contenthash].js",
    clean:true,
    assetModuleFilename: "images/[name][ext]",
  },
  module: {
    rules: [
      {
        test: /\.css$/, use: [MiniCssExtractPlugin.loader, "css-loader"]},
      {
        test: /\.js$/,
        exclude:/node_modules/,
        use: {
          loader: "babel-loader",
          options:{
            presets: ["@babel/preset-env"]
          },
        },
      },
      {
        test: /\.{png|svg|jpg|jpeg|gif}$/i,
        type: "assets/resource",
      },
      {
        test: /\.html$/i,
        loader: "html-loader",
      },
    ],
  },
  plugins:[
    new HtmlWebpackPlugin({
      filename: "index.html",
      template: "src/index.html",
    }),
    new MiniCssExtractPlugin({
      filename: "css/[name].[contenthash].css",
      chunkFilename: "[id].[contenthash].css",
    }),
    new CopyPlugin({
      patterns: [{from: "./public", to: path.resolve(__dirname, "dist")}]
    }),
    new Dotenv({
      path: './.env',
      safe: true,
    }),
  ],
  optimization: {
    moduleIds: "deterministic",
    runtimeChunk: "single",
    splitChunks: {
      cacheGroups: {
        vendor:{
          test: /[\\/]node_modules[\\/]/,
          name: "vendors",
          chunks: "all",
        },
      },
    },
    minimizer: [new CssMinimizerPlugin()],
  },
  devServer: {
    static: {
      directory: path.resolve(__dirname, "dist"),
    },
    port: 3000,
    open: true,
    hot: true,
    compress: true,
    historyApiFallback: true,
  },
  devtool: "source-map",
};