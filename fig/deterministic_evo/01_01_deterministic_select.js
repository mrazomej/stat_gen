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
      };var element = document.getElementById("e7428b3c-a8b2-4634-9eab-4811b97c66e4");
      if (element == null) {
        console.error("Bokeh: ERROR: autoload.js configured with elementid 'e7428b3c-a8b2-4634-9eab-4811b97c66e4' but no matching script tag was found. ")
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
                    
                  var docs_json = '{"1794cf19-f7a8-4206-8033-63a2685056fe":{"roots":{"references":[{"attributes":{"children":[{"id":"1002","type":"Slider"},{"id":"1001","type":"Slider"},{"id":"1005","subtype":"Figure","type":"Plot"}]},"id":"1042","type":"Column"},{"attributes":{"text":""},"id":"1044","type":"Title"},{"attributes":{},"id":"1020","type":"BasicTicker"},{"attributes":{},"id":"1045","type":"BasicTickFormatter"},{"attributes":{"dimension":1,"ticker":{"id":"1020","type":"BasicTicker"}},"id":"1023","type":"Grid"},{"attributes":{"callback":null,"end":1.05,"start":-0.05},"id":"1008","type":"Range1d"},{"attributes":{},"id":"1047","type":"BasicTickFormatter"},{"attributes":{"source":{"id":"1003","type":"ColumnDataSource"}},"id":"1041","type":"CDSView"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{"args":{"sSlider":{"id":"1001","type":"Slider"},"source":{"id":"1003","type":"ColumnDataSource"},"xoSlider":{"id":"1002","type":"Slider"}},"code":"\\n// Variable definition\\nvar data = source.data; \\nvar s_select = sSlider.value;\\nvar x_init = xoSlider.value;\\n\\n// Function definition\\nfunction x_select(t, x_init, s_select){\\n    var updated_val =  x_init * Math.exp(s_select * t) / \\n    (1 + x_init * (Math.exp(s_select * t) - 1));\\n    return updated_val;\\n}\\n\\n// Update values using a for loop (since I don&#x27;t know how to do \\n// vectorized oprations)\\nvar updated_allele = []; // temporary variable to update values\\nfor (var i = 0; i &lt; data[&#x27;time&#x27;].length; i++){\\n    updated_allele[i] = x_select(data[&#x27;time&#x27;][i], x_init, s_select);\\n}\\n// update x_allele column entry in source\\ndata[&#x27;x_allele&#x27;] = updated_allele\\n\\n// Emit data source for plot to be updated\\nsource.change.emit();\\n"},"id":"1004","type":"CustomJS"},{"attributes":{},"id":"1049","type":"UnionRenderers"},{"attributes":{"callback":{"id":"1004","type":"CustomJS"},"end":0.03,"format":"0[.]0000","js_property_callbacks":{"change:value":[{"id":"1004","type":"CustomJS"}]},"start":-0.03,"step":0.0001,"title":"s","value":0.01},"id":"1001","type":"Slider"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":2,"x":{"field":"time"},"y":{"field":"x_allele"}},"id":"1039","type":"Line"},{"attributes":{"below":[{"id":"1014","type":"LinearAxis"}],"center":[{"id":"1018","type":"Grid"},{"id":"1023","type":"Grid"}],"left":[{"id":"1019","type":"LinearAxis"}],"plot_height":275,"plot_width":300,"renderers":[{"id":"1040","type":"GlyphRenderer"}],"title":{"id":"1044","type":"Title"},"toolbar":{"id":"1030","type":"Toolbar"},"x_range":{"id":"1006","type":"DataRange1d"},"x_scale":{"id":"1010","type":"LinearScale"},"y_range":{"id":"1008","type":"Range1d"},"y_scale":{"id":"1012","type":"LinearScale"}},"id":"1005","subtype":"Figure","type":"Plot"},{"attributes":{"data_source":{"id":"1003","type":"ColumnDataSource"},"glyph":{"id":"1038","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1039","type":"Line"},"selection_glyph":null,"view":{"id":"1041","type":"CDSView"}},"id":"1040","type":"GlyphRenderer"},{"attributes":{},"id":"1050","type":"Selection"},{"attributes":{},"id":"1024","type":"PanTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1051","type":"BoxAnnotation"},{"attributes":{},"id":"1025","type":"WheelZoomTool"},{"attributes":{"callback":{"id":"1004","type":"CustomJS"},"end":1,"js_property_callbacks":{"change:value":[{"id":"1004","type":"CustomJS"}]},"start":0,"step":0.01,"title":"x\\u2092","value":0.1},"id":"1002","type":"Slider"},{"attributes":{"overlay":{"id":"1051","type":"BoxAnnotation"}},"id":"1026","type":"BoxZoomTool"},{"attributes":{},"id":"1012","type":"LinearScale"},{"attributes":{},"id":"1027","type":"SaveTool"},{"attributes":{"callback":null},"id":"1006","type":"DataRange1d"},{"attributes":{},"id":"1028","type":"ResetTool"},{"attributes":{"axis_label":"time (a.u.)","formatter":{"id":"1047","type":"BasicTickFormatter"},"ticker":{"id":"1015","type":"BasicTicker"}},"id":"1014","type":"LinearAxis"},{"attributes":{},"id":"1015","type":"BasicTicker"},{"attributes":{},"id":"1029","type":"HelpTool"},{"attributes":{"ticker":{"id":"1015","type":"BasicTicker"}},"id":"1018","type":"Grid"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1024","type":"PanTool"},{"id":"1025","type":"WheelZoomTool"},{"id":"1026","type":"BoxZoomTool"},{"id":"1027","type":"SaveTool"},{"id":"1028","type":"ResetTool"},{"id":"1029","type":"HelpTool"}]},"id":"1030","type":"Toolbar"},{"attributes":{"axis_label":"allele frequency","formatter":{"id":"1045","type":"BasicTickFormatter"},"ticker":{"id":"1020","type":"BasicTicker"}},"id":"1019","type":"LinearAxis"},{"attributes":{"line_color":"#1f77b4","line_width":2,"x":{"field":"time"},"y":{"field":"x_allele"}},"id":"1038","type":"Line"},{"attributes":{"callback":null,"data":{"time":{"__ndarray__":"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","dtype":"float64","shape":[500]},"x_allele":{"__ndarray__":"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","dtype":"float64","shape":[500]}},"selected":{"id":"1050","type":"Selection"},"selection_policy":{"id":"1049","type":"UnionRenderers"}},"id":"1003","type":"ColumnDataSource"}],"root_ids":["1042"]},"title":"Bokeh Application","version":"1.2.0"}}';
                  var render_items = [{"docid":"1794cf19-f7a8-4206-8033-63a2685056fe","roots":{"1042":"e7428b3c-a8b2-4634-9eab-4811b97c66e4"}}];
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