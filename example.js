function start(){
  holol = {
    tagName:"DIV",
    content:"",
    name:"holol",
    attributes:[],
    tagChilds:[{
      tagName:"H1",
      name:"holamen",
      content:"Hola mundo",
      attributes:[],
      tagChilds:[{
        tagName:"STRONG",
        content:"Hello",
        attributes:[],
        tagChilds:[]
      }]
    }]
  }
  holax = {
    tagName:"FORM",
    name:"miformu",
    attributes:[],
    tagChilds:[{
      name:"miInput",
      tagName:"INPUT",
      content:"",
      attributes:[{attrName:"type",attr:"button"},
        {attrName:"value",attr:"Desaparecer"},
        {attrName:"onclick",attr:"holamundo.setData(null)"}
      ],
      tagChilds:[]
    }]
  }
holamundo = new DeepModules(holol);
pregunta = new DeepModules(holax)
holamundo.firstRender();
pregunta.firstRender();
}
