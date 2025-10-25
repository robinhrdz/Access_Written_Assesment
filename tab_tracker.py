from streamlit.components.v1 import html

def inject_tab_tracker():
    html("""
    <script>
    (function() {
        if (!sessionStorage.getItem('tab_switches')) {
            sessionStorage.setItem('tab_switches', '0');
        }
        
        let count = parseInt(sessionStorage.getItem('tab_switches') || '0');
        let isHidden = false;
        
        function updateURL() {
            const url = new URL(window.parent.location.href);
            url.searchParams.set('tab_count', count);
            window.parent.history.replaceState({}, '', url);
        }
        
        function incrementCounter() {
            count++;
            sessionStorage.setItem('tab_switches', count.toString());
            updateURL();
            console.log('Tab switch detected. Total:', count);
        }
        
        document.addEventListener("visibilitychange", function() {
            if (document.visibilityState === "hidden" && !isHidden) {
                isHidden = true;
                incrementCounter();
            } else if (document.visibilityState === "visible") {
                isHidden = false;
            }
        });
        
        window.addEventListener("blur", function() {
            incrementCounter();
        });
        
        updateURL();
        console.log('Tab detector started. Count:', count);
    })();
    </script>
    """, height=0)

def reset_tab_counter():
    html("""
    <script>
    sessionStorage.setItem('tab_switches', '0');
    const url = new URL(window.parent.location.href);
    url.searchParams.delete('tab_count');
    window.parent.history.replaceState({}, '', url);
    console.log('Counter reset');
    </script>
    """, height=0)

def get_tab_count():
    import streamlit as st
    query_params = st.query_params
    try:
        if 'tab_count' in query_params:
            return int(query_params['tab_count'])
    except:
        pass
    return 0