/**
 * Created by deathnerd on 6/1/15.
 */
var gulp = require('gulp');
var browserSync = require('browser-sync').create();

// start the browserSync instance
gulp.task('browserSync', function(){
    browserSync.init({
    	server: {
    		baseDir: "."
    	},
        files: [
            "images/**",
            "scripts/**",
            "elements/**",
            "index.html",
            "styles/**"
        ]
    })
});