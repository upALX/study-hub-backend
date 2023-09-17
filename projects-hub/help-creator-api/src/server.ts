import {fastify} from 'fastify';
import { getAllPromptsResource } from './resource/get-all-prompts-resource';
import { postUploadVideoResource } from './resource/post-upload-videos-resource';

const app = fastify()

// GET 
app.register(getAllPromptsResource)

//POST 
app.register(postUploadVideoResource)


app.listen({port:3333}).then(()=>{
    console.log('Server running...')
})