/*******************

Include required scripts
```
<script src="js/paged.polyfill.js"></script>
<script src="js/mustache.js"></script>
<script src="js/paged-mustache.js"></script>
```

Use `<script>const DATA = {name:"world"}</script>` 
Use `<script src="my-partial.mustache" type="x-tmpl-mustache"></script>` in head to declare a partial.
Use `<script src="my-template.mustache" type="x-tmpl-mustache"></script>` in body to load a template.
Both can be used without the `src=""` attribute, writing the mustache code directly inside the script tag.

*******************/



const scriptElementToText = async (element) => {
    if(element.src){
        let response = await fetch(element.src);
        return await response.text();
    }
    return element.innerHTML;
}


class pagedMustache extends Paged.Handler {
    constructor(chunker, polisher, caller) {
      super(chunker, polisher, caller);
    }
  
    beforeParsed(content) {
        return (async () => {
            let partials = document.querySelectorAll('head [type=x-tmpl-mustache]');
            let templates = content.querySelectorAll('[type=x-tmpl-mustache]');

            let partialsCollection = {};
            for (const el of partials) {
                partialsCollection[el.id] = await scriptElementToText(el)
            }

            for (const el of templates) {
                let template = await scriptElementToText(el)
                console.log(template)
                let rendered = Mustache.render(template, DATA, partialsCollection);
                let parsed = new DOMParser().parseFromString(rendered, 'text/html').body.childNodes;
                console.log(parsed)
                el.after(...parsed);    
            }
        })();
    }
}

Paged.registerHandlers(pagedMustache);