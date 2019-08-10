(function() {
  var fn = function() {
    
    (function(root) {
      function now() {
        return new Date();
      }
    
      var force = false;
    
      if (typeof root._bokeh_onload_callbacks === "undefined" || force === true) {
        root._bokeh_onload_callbacks = [];
        root._bokeh_is_loading = undefined;
      }
    
      
      
    
      
      
    
      function run_callbacks() {
        try {
          root._bokeh_onload_callbacks.forEach(function(callback) {
            if (callback != null)
              callback();
          });
        } finally {
          delete root._bokeh_onload_callbacks
        }
        console.debug("Bokeh: all callbacks have finished");
      }
    
      function load_libs(css_urls, js_urls, callback) {
        if (css_urls == null) css_urls = [];
        if (js_urls == null) js_urls = [];
    
        root._bokeh_onload_callbacks.push(callback);
        if (root._bokeh_is_loading > 0) {
          console.debug("Bokeh: BokehJS is being loaded, scheduling callback at", now());
          return null;
        }
        if (js_urls == null || js_urls.length === 0) {
          run_callbacks();
          return null;
        }
        console.debug("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
        root._bokeh_is_loading = css_urls.length + js_urls.length;
    
        function on_load() {
          root._bokeh_is_loading--;
          if (root._bokeh_is_loading === 0) {
            console.debug("Bokeh: all BokehJS libraries/stylesheets loaded");
            run_callbacks()
          }
        }
    
        function on_error() {
          console.error("failed to load " + url);
        }
    
        for (var i = 0; i < css_urls.length; i++) {
          var url = css_urls[i];
          const element = document.createElement("link");
          element.onload = on_load;
          element.onerror = on_error;
          element.rel = "stylesheet";
          element.type = "text/css";
          element.href = url;
          console.debug("Bokeh: injecting link tag for BokehJS stylesheet: ", url);
          document.body.appendChild(element);
        }
    
        for (var i = 0; i < js_urls.length; i++) {
          var url = js_urls[i];
          var element = document.createElement('script');
          element.onload = on_load;
          element.onerror = on_error;
          element.async = false;
          element.src = url;
          console.debug("Bokeh: injecting script tag for BokehJS library: ", url);
          document.head.appendChild(element);
        }
      };var element = document.getElementById("fb4b236e-cd8b-4a15-96dc-cbf64700a05b");
      if (element == null) {
        console.error("Bokeh: ERROR: autoload.js configured with elementid 'fb4b236e-cd8b-4a15-96dc-cbf64700a05b' but no matching script tag was found. ")
        return false;
      }
    
      function inject_raw_css(css) {
        const element = document.createElement("style");
        element.appendChild(document.createTextNode(css));
        document.body.appendChild(element);
      }
    
      var js_urls = ["https://cdn.pydata.org/bokeh/release/bokeh-1.2.0.min.js", "https://cdn.pydata.org/bokeh/release/bokeh-widgets-1.2.0.min.js", "https://cdn.pydata.org/bokeh/release/bokeh-tables-1.2.0.min.js", "https://cdn.pydata.org/bokeh/release/bokeh-gl-1.2.0.min.js"];
      var css_urls = ["https://cdn.pydata.org/bokeh/release/bokeh-1.2.0.min.css", "https://cdn.pydata.org/bokeh/release/bokeh-widgets-1.2.0.min.css", "https://cdn.pydata.org/bokeh/release/bokeh-tables-1.2.0.min.css"];
    
      var inline_js = [
        function(Bokeh) {
          Bokeh.set_log_level("info");
        },
        
        function(Bokeh) {
          
        },
        
        function(Bokeh) {
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json = '{"f272a599-1dd6-44bc-97ed-e7405ac2ac39":{"roots":{"references":[{"attributes":{"callback":null},"id":"1007","type":"DataRange1d"},{"attributes":{"callback":null,"end":1,"js_property_callbacks":{"change:value":[{"id":"1005","type":"CustomJS"}]},"start":0,"step":0.01,"title":"x\\u2092","value":0.01},"id":"1003","type":"Slider"},{"attributes":{"callback":null,"end":0.03,"format":"0[.]0000","js_property_callbacks":{"change:value":[{"id":"1005","type":"CustomJS"}]},"start":0,"step":0.0001,"title":"\\u03bc _aA","value":0.01},"id":"1002","type":"Slider"},{"attributes":{"callback":null,"end":1.05,"start":-0.05},"id":"1009","type":"Range1d"},{"attributes":{"children":[{"id":"1003","type":"Slider"},{"id":"1001","type":"Slider"},{"id":"1002","type":"Slider"},{"id":"1006","subtype":"Figure","type":"Plot"}]},"id":"1043","type":"Column"},{"attributes":{"axis_label":"allele frequency","formatter":{"id":"1048","type":"BasicTickFormatter"},"ticker":{"id":"1021","type":"BasicTicker"}},"id":"1020","type":"LinearAxis"},{"attributes":{},"id":"1021","type":"BasicTicker"},{"attributes":{"text":""},"id":"1045","type":"Title"},{"attributes":{"dimension":1,"ticker":{"id":"1021","type":"BasicTicker"}},"id":"1024","type":"Grid"},{"attributes":{},"id":"1046","type":"BasicTickFormatter"},{"attributes":{"callback":null,"data":{"time":{"__ndarray__":"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","dtype":"float64","shape":[300]},"x_allele":{"__ndarray__":"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","dtype":"float64","shape":[300]}},"selected":{"id":"1050","type":"Selection"},"selection_policy":{"id":"1051","type":"UnionRenderers"}},"id":"1004","type":"ColumnDataSource"},{"attributes":{"source":{"id":"1004","type":"ColumnDataSource"}},"id":"1042","type":"CDSView"},{"attributes":{"line_color":"#1f77b4","line_width":2,"x":{"field":"time"},"y":{"field":"x_allele"}},"id":"1039","type":"Line"},{"attributes":{"args":{"muAaSlider":{"id":"1001","type":"Slider"},"muaASlider":{"id":"1002","type":"Slider"},"source":{"id":"1004","type":"ColumnDataSource"},"xoSlider":{"id":"1003","type":"Slider"}},"code":"\\n// Variable definition\\nvar data = source.data; \\nvar x_init = xoSlider.value;\\nvar mu_Aa = muAaSlider.value;\\nvar mu_aA = muaASlider.value;\\n\\n// Function definition\\nfunction x_select(t, x_init, mu_Aa, mu_aA){\\n    var mu = mu_Aa + mu_aA;\\n    var updated_val =  mu_aA / mu -\\n                       (mu_aA - mu * x_init) * Math.exp(- mu * t) / mu\\n    return updated_val;\\n}\\n\\n// Update values using a for loop (since I don&#x27;t know how to do \\n// vectorized oprations)\\nvar updated_allele = []; // temporary variable to update values\\nfor (var i = 0; i &lt; data[&#x27;time&#x27;].length; i++){\\n    updated_allele[i] = x_select(data[&#x27;time&#x27;][i], x_init, mu_Aa, mu_aA);\\n}\\n// update x_allele column entry in source\\ndata[&#x27;x_allele&#x27;] = updated_allele\\n\\n// Emit data source for plot to be updated\\nsource.change.emit();\\n"},"id":"1005","type":"CustomJS"},{"attributes":{},"id":"1048","type":"BasicTickFormatter"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":2,"x":{"field":"time"},"y":{"field":"x_allele"}},"id":"1040","type":"Line"},{"attributes":{},"id":"1011","type":"LinearScale"},{"attributes":{},"id":"1050","type":"Selection"},{"attributes":{"callback":null,"end":0.03,"format":"0[.]0000","js_property_callbacks":{"change:value":[{"id":"1005","type":"CustomJS"}]},"start":0,"step":0.0001,"title":"\\u03bc _Aa","value":0.003},"id":"1001","type":"Slider"},{"attributes":{"data_source":{"id":"1004","type":"ColumnDataSource"},"glyph":{"id":"1039","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1040","type":"Line"},"selection_glyph":null,"view":{"id":"1042","type":"CDSView"}},"id":"1041","type":"GlyphRenderer"},{"attributes":{},"id":"1051","type":"UnionRenderers"},{"attributes":{"below":[{"id":"1015","type":"LinearAxis"}],"center":[{"id":"1019","type":"Grid"},{"id":"1024","type":"Grid"}],"left":[{"id":"1020","type":"LinearAxis"}],"plot_height":275,"plot_width":300,"renderers":[{"id":"1041","type":"GlyphRenderer"}],"title":{"id":"1045","type":"Title"},"toolbar":{"id":"1031","type":"Toolbar"},"x_range":{"id":"1007","type":"DataRange1d"},"x_scale":{"id":"1011","type":"LinearScale"},"y_range":{"id":"1009","type":"Range1d"},"y_scale":{"id":"1013","type":"LinearScale"}},"id":"1006","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"1025","type":"PanTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1052","type":"BoxAnnotation"},{"attributes":{},"id":"1026","type":"WheelZoomTool"},{"attributes":{"overlay":{"id":"1052","type":"BoxAnnotation"}},"id":"1027","type":"BoxZoomTool"},{"attributes":{"ticker":{"id":"1016","type":"BasicTicker"}},"id":"1019","type":"Grid"},{"attributes":{},"id":"1028","type":"SaveTool"},{"attributes":{},"id":"1013","type":"LinearScale"},{"attributes":{},"id":"1029","type":"ResetTool"},{"attributes":{},"id":"1016","type":"BasicTicker"},{"attributes":{"axis_label":"time (a.u.)","formatter":{"id":"1046","type":"BasicTickFormatter"},"ticker":{"id":"1016","type":"BasicTicker"}},"id":"1015","type":"LinearAxis"},{"attributes":{},"id":"1030","type":"HelpTool"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1025","type":"PanTool"},{"id":"1026","type":"WheelZoomTool"},{"id":"1027","type":"BoxZoomTool"},{"id":"1028","type":"SaveTool"},{"id":"1029","type":"ResetTool"},{"id":"1030","type":"HelpTool"}]},"id":"1031","type":"Toolbar"}],"root_ids":["1043"]},"title":"Bokeh Application","version":"1.2.0"}}';
                  var render_items = [{"docid":"f272a599-1dd6-44bc-97ed-e7405ac2ac39","roots":{"1043":"fb4b236e-cd8b-4a15-96dc-cbf64700a05b"}}];
                  root.Bokeh.embed.embed_items(docs_json, render_items);
                
                  }
                  if (root.Bokeh !== undefined) {
                    embed_document(root);
                  } else {
                    var attempts = 0;
                    var timer = setInterval(function(root) {
                      if (root.Bokeh !== undefined) {
                        embed_document(root);
                        clearInterval(timer);
                      }
                      attempts++;
                      if (attempts > 100) {
                        console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                        clearInterval(timer);
                      }
                    }, 10, root)
                  }
                })(window);
              });
            };
            if (document.readyState != "loading") fn();
            else document.addEventListener("DOMContentLoaded", fn);
          })();
        },
        function(Bokeh) {} // ensure no trailing comma for IE
      ];
    
      function run_inline_js() {
        
        for (var i = 0; i < inline_js.length; i++) {
          inline_js[i].call(root, root.Bokeh);
        }
        
      }
    
      if (root._bokeh_is_loading === 0) {
        console.debug("Bokeh: BokehJS loaded, going straight to plotting");
        run_inline_js();
      } else {
        load_libs(css_urls, js_urls, function() {
          console.debug("Bokeh: BokehJS plotting callback run at", now());
          run_inline_js();
        });
      }
    }(window));
  };
  if (document.readyState != "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
})();