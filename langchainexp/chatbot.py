import gradio as gr

def predict(inp, history=[]):
    output='<From MODEL>'
    history.append((inp, output))
    return history, history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    state = gr.State([])

    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)

    txt.submit(predict, [txt, state], [chatbot, state])
            
if __name__ == "__main__":
    demo.launch(share=True)