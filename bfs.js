const grafo = []
function addvertice(v){
    const vertice={
        valor:v,
        arestas:[]
    }
    grafo.push(vertice)
}
function addarestas(v1,v2){
    for (var i=0; i < grafo.length; i++){
        if(grafo[i].valor == v1){
            grafo[i].arestas.push(v2)
        }
    }
    for (var i=0; i < grafo.length; i++){
        if(grafo[i].valor == v2){
            grafo[i].arestas.push(v1)
        }
    }

}
function getadj(v){
    for (var i=0; i < grafo.length; i++){
        if(grafo[i].valor == v){
            return (grafo[i].arestas)   
        }
    } 
}


function BFS(v,v2){
    var cor = []
    var fila =[]
    var pred = []
    for (var i=0; i<grafo.length; i++){
        cor[grafo[i].valor] = 'branco' 
    }

    fila.push(v)

    for (var i=0; i<grafo.length; i++){
        pred[grafo[i].valor] = null
    }

        while (fila.length != 0){
            var u = fila.shift()
            var vizinhos = getadj(u)
            cor[u]='cinza'
                for (var i=0; i<vizinhos.length; i++){
                    var w = vizinhos[i]
                    if(cor[w] === 'branco'){
                        cor[w] = 'cinza'
                        pred[w] = u
                        fila.push(w)
                    }
                } 
                cor[u]='preto' 
                console.log(u) 
        }


        var cam =[]
        cam.push(v2)
        var x = pred[v2]
        while (x !== v) {
            cam.push(x)
            x = pred[x]
        }
        cam.push(v)
        console.log(cam)
}



addvertice('Oradea')
addvertice('Zerind ')
addvertice('Arad')
addvertice('Timisoara')
addvertice('Lugoj')
addvertice('Mehadia')
addvertice('Dobreta')
addvertice('Craiova')
addvertice('RV')
addvertice('Sibiu')
addvertice('Fagaras')
addvertice('Pitesti')
addvertice('Bucharest')
addvertice('Giurgiu')
addvertice('Urziceni')
addvertice('Eforie')
addvertice('Hirsova')
addvertice('Vaslui')
addvertice('Iasi')
addvertice('Neamt')

addarestas('Oradea','Zerind')
addarestas('Oradea','Sibiu')
addarestas('Arad','Zerind')
addarestas('Arad','Sibiu')
addarestas('Arad','Timisoara')
addarestas('Lugoj','Timisoara')
addarestas('Lugoj','Mehadia')
addarestas('Lugoj','Mehadia')
addarestas('Dobreta','Mehadia')
addarestas('Dobreta','Craiova')
addarestas('RV','Craiova')
addarestas('Pitesti','Craiova')
addarestas('RV','Sibiu')
addarestas('RV','Pitesti')
addarestas('Fagaras','Sibiu')
addarestas('Fagaras','Bucharest')
addarestas('Pitesti','Bucharest')
addarestas('Giurgiu','Bucharest')
addarestas('Urziceni','Bucharest')
addarestas('Urziceni','Hirsova')
addarestas('Urziceni','Vaslui')
addarestas('Eforie','Hirsova')
addarestas('Iasi','Vaslui')
addarestas('Iasi','Neamt')



BFS('Arad','Bucharest')
