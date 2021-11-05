<script nonce="KJdUZ6KtC14Ns2VX+chlpC7SUHCbLzFrXU+NNupwPEY=" type="text/javascript">
            $(function(){
              var hostname = window.location.hostname;
              if (hostname != 'checkout.shopify.com' && hostname != 'app.shopify.com') {
                var re = /\.(shopify|shopifyadmin)\.com$/;

                if (hostname.match(re)) {
                  var myshopifyDomain = encodeURI(hostname.replace(re,".myshopify.com"));
                  var href = encodeURI(window.location.href.replace(hostname, myshopifyDomain));
                  $("#did-you-mean-link").attr("href", href);
                  $("#did-you-mean-link").text(myshopifyDomain);
                  $("#shop-not-found").hide();
                  $("#did-you-mean-msg").show();
                } else if (!hostname.match(/\.myshopify\.com$/) && true) {
                  $("#one-step-left-hostname").text(hostname);
                  $("#shop-not-found").hide();
                  $("#one-step-left-msg").show();
                }
              }
            });
          </script>