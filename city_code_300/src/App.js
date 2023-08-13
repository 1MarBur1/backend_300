import './App.css'
import React, { useEffect, useState } from 'react'
import { Map, Placemark, YMaps, Button } from '@pbe/react-yandex-maps'
import { getAllPoints } from './shared/api/points'
import { Modal, Typography, Form, Input, Select } from 'antd'

const { Text } = Typography

function App() {
  const [allPoints, setAllPoints] = useState([])
  const [showModal, setShowModal] = useState(false)

  const [form] = Form.useForm();

  useEffect(() => {
    getAllPoints().then((data) => {
      setAllPoints(data)
    })
  }, [])

  const getColor = (type) => {
    switch (type) {
      case 'Грязь и мусор':
        return '#422121'
      case 'Свалка шин':
        return '#120e0e'
      case 'Разлив нефти':
        return '#731d1d'
      case 'Переполненные контейнеры':
        return '#153257'
      case 'Парковка на газонах':
        return '#42701c'
      case 'Несанкционированная торговля':
        return '#52472b'
      case 'Нарушение благоустройства':
        return '#cc6c4b'
      default:
        return null
    }
  }

  return (
    <div className="App">
      <YMaps>
        <div>
          <Map defaultState={{ center: [56.838010, 60.597465], zoom: 15 }} style={{ width: '100vw', height: '100vh' }}>
            <Button
              options={{ maxWidth: 128, selectOnClick: false }}
              onClick={() => setShowModal(true)}
              data={{ content: "Создать метку" }}
            />
            {allPoints?.map((item) => (
              <Placemark 
                modules={["geoObject.addon.balloon"]}
                defaultGeometry={item.location.split(', ')} 
                properties={{
                  balloonContentHeader: item.name,
                  balloonContentBody: `
                    <div style="display: flex; gap: 10px">
                      <p>${item.description}</p>
                      <img src="${item.photo}" width="100px" height="100px" />
                    </div>
                  `,
                  balloonContentFooter: item.type,
                }}
                options={{
                  iconColor: getColor(item.type)
                }} />
            ))}
          </Map>
        </div>
      </YMaps>

      <Modal 
        onCancel={() => setShowModal(false)}
        onOk={() => setShowModal(false)}
        open={showModal}
      >
        <Text>
          Создать новую метку
        </Text>

        <Form 
          style={{ marginTop: '10px' }} 
          form={form} 
          onFinish={(values) => console.log(values)}
        >
          <Form.Item label='Изображение'>
            <Input placeholder='Вставьте ссылку на изображение' />
          </Form.Item>
          <Form.Item label='Название'>
            <Input placeholder='Название' />
          </Form.Item>
          <Form.Item label='Описание'>
            <Input placeholder='Описание' />
          </Form.Item>
          <Form.Item label='Категория'>
            <Select 
              placeholder='Категория'
              options={[{
                label: 'Грязь и мусор',
                value: 'Грязь и мусор'
              }, {
                label: 'Свалка шин',
                value: 'Свалка шин'
              }, {
                label: 'Разлив нефти',
                value: 'Разлив нефти'
              }, {
                label: 'Переполненные контейнеры',
                value: 'Переполненные контейнеры'
              }, {
                label: 'Парковка на газонах',
                value: 'Парковка на газонах'
              }, {
                label: 'Несанкционированная торговля',
                value: 'Несанкционированная торговля'
              }, {
                label: 'Нарушение благоустройства',
                value: 'Нарушение благоустройства'
              }]} />
          </Form.Item>
          <Form.Item label='Адрес'>
            <Input placeholder='Адрес' />
          </Form.Item>

          <button type='submit'>
              save
          </button>
        </Form>
      </Modal>
    </div>
  )
}

export default App;