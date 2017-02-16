(function() {
    'use strict';

    $(onReady);

    function onReady() {
        $('.ctrl-domains').each(function() {
            var domainsEl = $(this);

            domainsEl.tagsManager({
                tagClass: 'label label-success',
                hiddenTagListName: 'hosts',
                prefilled: domainsEl.val()
            });

        });

        $('.ctrl-domain-form').on('submit', function() {
            var visibleInput = $(this).find('.ctrl-domains');
            if (!visibleInput.val()) return;

            var hiddenInput = $(this).find('[type=hidden]');
            hiddenInput[0].value += ',' + visibleInput.val();
        });


        $('#delete-account').on('click', function() {
            if ($('.plan-card').length && $('.plan-card > .price-tag').html() !== 'Trial') {
                alert('Before deleting your account, please cancel your active subscription(s)');
                return false;
            }
            if (confirm('Are you sure you want to delete your account?\nThis action cannot be undone.')) {
                $('#delete-account-form').submit();
            }
            return false;
        });
    }

})();


