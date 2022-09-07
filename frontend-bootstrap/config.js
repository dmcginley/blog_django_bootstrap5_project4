const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: "./src/js/index.js",
    mode: "development",
    output: {
        filename: "dist/main.js",
        path: "/home/donnchadh/HTML_Projects/code_projects/Project4_django-bootstrap5/techblog_project/library/static/library/js",
    },
    module: {
        rules: [
            {
                test: /\.(scss)$/,
                use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
            }
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "../css/index.css",
        })
    ]
};
