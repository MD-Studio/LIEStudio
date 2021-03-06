import * as gulp from 'gulp';
import * as runSequence from 'run-sequence';
import * as requireDir from 'require-dir';

requireDir('./gulp/tasks');

gulp.task('serve', callback =>
    runSequence('build', 'watch', callback)
);

gulp.task('build', callback =>
    runSequence('clean', ['copy:dist', 'ts:dist', 'sass:dist', 'bower:dist'], 'inject', 'server:init', callback)
);

gulp.task('compile', callback =>
    runSequence('clean', ['copy:dist', 'ts:dist', 'sass:dist', 'bower:dist'], 'inject', callback)
);