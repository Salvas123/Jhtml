class DeepModules{
  //construct(jsonfor html div, div id)
  constructor(data){
    this.data = data;
  }

  firstRender(){
    parseJSONforHtml(this.data);
  }
  //draw  module
  render(){
    let elem = document.getElementById(this.old.name);
    elem.parentNode.removeChild(elem);
    parseJSONforHtml(this.data);
  }

  getData(){
    return this.data;
  }

  setData(newData){
    this.old = this.data;
    this.data = newData;
    this.render();
  }
}

function parseJSONforHtml(data){
  base= document.createElement(data.tagName);
  base.innerHTML = data.content;
  base.setAttribute("id",data.name)
  document.getElementById("theContainer").appendChild(base);
  let i = 0;
  for(i in data.tagChilds){
    parseoSalseante(data.tagChilds[i],base);
  }
  i = 0;
  for(i in data.attributes){
    attributesAdd(data.attributes[i],base);
  }
}

function attributesAdd(el,attrTag){
  if(el.attrName){
    if (typeof el.attrName == 'string'){
      if(el.attrName.toLowerCase() != "id")attrTag.setAttribute(el.attrName,el.attr);
    }
  }
}

function parseoSalseante(el,container){
  let ele = document.createElement(el.tagName);
  ele.innerHTML = el.content;
  ele.setAttribute("id",el.name)
  let i = 0;
  for (i in el.attributes){
    attributesAdd(el.attributes[i],ele);
  }
  container.appendChild(ele);
  i = 0;
  for (i in el.tagChilds){
    if(el.tagChilds[0])parseoSalseante(el.tagChilds[i],ele);
  }
}
