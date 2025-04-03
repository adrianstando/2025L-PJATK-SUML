import gradio as gr
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model


MODEL_PATH = "mnist_model.keras"
model = load_model(MODEL_PATH)


# Predict function
def predict(image):
    # Expand the dimensions of the image to match the input shape of the model
    image = np.expand_dims(image, axis=0)
    
    # Make prediction
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions, axis=1)[0]
    
    # Get the probabilities for each class
    probabilities = predictions[0]
    
    return gr.update(value=str(predicted_class)), gr.update(value={str(i): float(prob) for i, prob in enumerate(probabilities)})


# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# MNIST Digit Classification")
    gr.Markdown("Draw a digit in the box below and click 'Predict' to see the result.")
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="numpy", label="Input Image", image_mode="L")
            predict_button = gr.Button("Predict from file")
            
        with gr.Column():
            predicted_class_output = gr.Textbox(label="Predicted Class", interactive=False)
            probabilities_output = gr.Label(label="Probabilities")

    predict_button.click(predict, inputs=image_input, outputs=[predicted_class_output, probabilities_output])


# Launch the app
if __name__ == "__main__":
    demo.launch()
