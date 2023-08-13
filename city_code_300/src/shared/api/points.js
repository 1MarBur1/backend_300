import axios from 'axios'

const getAllPoints = async () => {
    const response = await axios.get('http://127.0.0.1:8000/points')

    const data = await response.data
    
    return data
} 

const createPoint = async (createData) => {
    const response = await axios.post('http://127.0.0.1:8000/add_point/', createData)

    const data = await response.data
    
    return data
} 

export {
    getAllPoints,
    createPoint
}