import {fastify} from 'fastify';
import { getAllPromptsResource } from './resource/get-all-prompts';

const app = fastify()

app.register(getAllPromptsResource)

app.listen({port:3333}).then(()=>{
    console.log('Server running...')
})