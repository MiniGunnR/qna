$(function() {

    $(document).on('click', '.heart', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');

        $.get($href, function(data, status) {
            if (status === 'success') {
                if ($this.children().hasClass('red')) {
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                } else {
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                }
            }
        });
    });

    $(document).on('click', '.flag', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');

        $.get($href, function(data, status) {
            if (status === 'success') {
                if ($this.children().hasClass('red')) {
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                } else {
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                }
            }
        });
    });

    $(document).on('click', '.ques-comments-show', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');
        var $id = $this.attr('data-item-id');
        var $comment_div = $('#ques-' + $id + '-comments');

        $.get($href, function(data, status) {
            if (status == 'success') {
                $comment_div.toggle();
            }
        });
    });

     $(document).on('click', '.ans-comments-show', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');
        var $id = $this.attr('data-item-id');
         var $comment_div = $('#ans-' + $id + '-comments');

        $.get($href, function(data, status) {
            if (status == 'success') {
                $comment_div.toggle();
            }
        });
    });
});
