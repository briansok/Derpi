var gulp = require('gulp');
var less = require('gulp-less');
var watch = require('gulp-watch');

gulp.task('default', ['less']);

gulp.task('watch', function() {
    gulp.watch('derpi/static/less/**/*.less', ['less'])
});

gulp.task('less', function() {
    return gulp.src('derpi/static/less/site.less')
	.pipe(less())
	.pipe(gulp.dest('./derpi/static/css'));
});
