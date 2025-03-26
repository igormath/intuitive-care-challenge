export interface Operadora{
    cnpj: string;
    razao_social: string;
    cep: string;
    ddd: string;
    telefone: string;
    endereco_eletronico: string;
}

async function getOperadora(terms:string): Promise<Operadora[]> {

    try{
        const response = await fetch(`http://127.0.0.1:8000/operadora/?query=${terms}`);
        const data = await response.json() as Operadora[];
        return data;
    } catch (e){
        console.error(e);
        return [];
    }   
}

export {getOperadora};
