import React from "react";
import Amplify from "aws-amplify";
import {AmplifyChatbot} from "@aws-amplify/ui-react";
import './App.css';

import awsconfig from './aws-exports';

Amplify.configure(awsconfig);

const App = () => (
  <AmplifyChatbot
    style={{alignSelf:'center', width:100 }}
    botName="trafficBot"    
    botTitle="Driving Tutor chatbot (spanish)"
    welcomeMessage="¡Hola!, ¿Cómo te puedo ayudar?"
    placeholder={'Escribe aquí!'}
  />
);

export default App;
