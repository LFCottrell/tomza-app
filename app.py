import dash
from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
import os
from dash import html, ctx
from dash.exceptions import PreventUpdate
import dash_core_components as dcc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <title>My Dash PWA</title>
        <link rel="manifest" href="/assets/manifest.json">  <!-- Link to the PWA manifest -->
        <meta name="theme-color" content="#000000">  <!-- Define theme color -->
        <script>
            // Register the service worker
            if ("serviceWorker" in navigator) {
                navigator.serviceWorker.register("/assets/service-worker.js")
                .then(() => console.log("Service Worker Registered"))
                .catch(err => console.error("Service Worker Registration Failed", err));
            }
        </script>
        {%config%}  <!-- Required placeholder for Dash -->
    </head>
    <body>
        <div id="react-entry-point">
            {%app_entry%}  <!-- Required placeholder for Dash layout -->
        </div>
        <footer>
            {%scripts%}  <!-- Required placeholder for Dash scripts -->
            {%renderer%}  <!-- Optional: Recommended for Dash client rendering -->
        </footer>
    </body>
</html>
'''


modal = dbc.Modal(
        [
            dbc.ModalHeader("Choose a Narrator", style={'text-align': 'center'}),
            dbc.ModalBody(
                html.Div([
                    html.Div(
                        html.Img(id='liam', src='assets/pictures/liam head.png',
                                 style={'width': '15vw', 'height': '15vh', 'cursor': 'pointer'}),
                        id='liam_div',
                        style={'width': '100%', 'display': 'flex', 'justify-content': 'center'}
                    ),
                    html.Div(
                        html.Img(id='maria', src='assets/pictures/liam head.png',
                                 style={'width': '15vw', 'height': '15vh', 'cursor': 'pointer'}),
                        id='maria_div',
                        style={'width': '100%', 'display': 'flex', 'justify-content': 'center'}
                    ),
                    html.Div(
                        html.Img(id='daddo', src='assets/pictures/liam head.png',
                                 style={'width': '15vw', 'height': '15vh', 'cursor': 'pointer'}),
                        id='daddo_div',
                        style={'width': '100%', 'display': 'flex', 'justify-content': 'center'}
                    ),
                    # Add other family members here...
                ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'})
            ),
            dbc.ModalFooter(
                dbc.Button("Close", id="close-modal", n_clicks=0, color="secondary")
            ),
        ],
        id="narrator-modal",
        is_open=False,  # Modal is closed by default
        centered=True,  # Center the modal on the screen
        size="lg",  # Large modal size
        style={'text-align': 'center'}
    )

app.layout = html.Div(
    [
    dcc.Store(id='story_store', storage_type='session'),
    # dbc.Row(
    #     dbc.Col([
    #         html.Img(src='assets/pictures/moon.png', style={'height':'10vh'}),
    #         html.Div(
    #             html.H1("Tomza's story app", style={'font-family':'Comic Sans MS', 'font-weight':'bold', 'color':'#008080'}), style = {'width':'100%', 'display':'flex', 'justify-content':'center', 'color':'white'})
    #         ], style={'display':'flex'}
    #     )
    # ),
    html.Br(),


    dbc.Row([
    #     dbc.Col([
    # # html.Div([
    # #     html.Div(
    # #         html.Img(id='peppa_pig_story', src='assets/pictures/peppa_pig_football.jpg', style={'height': '150px'}),
    # #         id='peppa_div',
    # #
    # #     )], style={'width': '75%', 'margin-left': '25%'}),
    # html.Div([
    #     # html.Div(
    #     #     html.H3('Narrator'), style={'background-color':'#ADD8E6', 'color':'white','display': 'flex', 'justify-content': 'center', 'align-items':'center','width':'17vw'}),
    #     html.Div(
    #         html.Img(id='liam', src='assets/pictures/liam head.png', style={'width':'15vw', 'height':'15vh'}), id='liam_div', style={'width':'100%','display':'flex', 'justify-content':'center'}
    #     ),
    #     html.Div(
    #         html.Img(id='maria', src='assets/pictures/liam head.png', style={'width':'15vw', 'height':'15vh'}), id='maria_div', style={'width':'100%','display':'flex', 'justify-content':'center'}),
    #     html.Div(
    #         html.Img(id='daddo', src='assets/pictures/liam head.png', style={'width':'15vw', 'height':'15vh'}), id='daddo_div', style={'width':'100%','display':'flex', 'justify-content':'center'}),
    #     html.Div(
    #         html.Img(id='bengo',src='assets/pictures/liam head.png', style={'width':'15vw', 'height':'15vh'}), id='bengo_div', style={'width':'100%','display':'flex', 'justify-content':'center'}),
    #     html.Div(
    #         html.Img(id='joseppi', src='assets/pictures/liam head.png', style={'width':'15vw', 'height':'15vh'}), id='joseph_div', style={'width':'100%','display':'flex', 'justify-content':'center'}),
    #     html.Div(
    #         html.Img(id='mumza', src='assets/pictures/liam head.png', style={'width':'15vw', 'height':'15vh'}), id='mumza_div', style={'width':'100%','display':'flex', 'justify-content':'center'})
    # ], id='voice-selection-div', style={'width':'100%', 'justify-content':'center', 'background-color':"#ADD8E6", 'border-radius':'100px'})], width = 2
    #     ),

        dbc.Col(
            html.Div([
                html.Div(modal),
                html.Div([
                    # Peppa Pig story
                    html.Div([
                        html.Img(id='peppa_pig_story',
                                 src='assets/pictures/peppa_pig_football.jpg',
                                 style={'height': '15vh', 'margin': '10px', 'border-radius': '500px', 'width': '10vw',
                                        'cursor': 'pointer'}),
                        html.P('Tom plays football with Peppa, who learns the offside rule...', style={'font-size': '15px','color': 'white', 'font-weight': 'bold', 'line-height':'5vh', 'margin-left':'2vw', 'margin-right':'2vw', 'margin-top':'3vh'})],
                        id='peppa_div', style={'border-radius':'50px', 'width':'25vw', 'height':'40vh', 'margin-left':'2.5vw', 'margin-right':'10vw', 'background-color':'pink', 'transition': 'all 0.3s ease',}, className='hover-effect'
                    ),
                    # Postman Pat story
                    html.Div([
                        html.Img(id='postman_pat_story',
                                 src='assets/pictures/Postman_Pat2webp.webp',
                                 style={'height': '15vh', 'border-radius': '150px', 'width': '10vw',
                                        'cursor': 'pointer', 'margin-top':'1vh'}),

                        html.P("Pats's van runs out of gas, but Tom suggests the underground to save the day...", style={'font-size': '15px','color': 'white', 'font-weight': 'bold', 'line-height':'5vh', 'margin-left':'2vw', 'margin-right':'2vw', 'margin-top':'3vh'})],
                        id='pat_div', style={'height':'40vh', 'background-color':'#ADD8E6', 'border-radius':'50px', 'width':'25vw'}, className='hover-effect'
                    ),
                    # Bowser story
                    html.Div([
                        html.Img(id='bowser_story',
                                 src='assets/pictures/bowser.webp',
                                 style={'height': '15vh', 'margin': '10px', 'border-radius': '100px',
                                        'cursor': 'pointer'}),
                        html.P("Baby Mario encounters Bowser, inspired by the gruffalo...", style={'font-size': '15px','color': 'white', 'font-weight': 'bold', 'line-height':'5vh', 'margin-left':'2vw', 'margin-right':'2vw', 'margin-top':'3vh'}),
                        ],
                        id='bowser_div', style={'height':'40vh', 'background-color':'#BFF4BE', 'border-radius':'50px', 'width':'25vw', 'margin-left':'10vw', 'margin-right':'2.5vw'}, className='hover-effect'
                    ),
                ], style={'width': '100%', 'text-align': 'center', 'display':'flex'}),  # Wrap first three in a row
                html.Hr(),

                # Paddington story on its own level
                html.Div([
                html.Div([
                    html.Img(id='paddington_story',
                             src='assets/pictures/paddington.webp',
                             style={'height': '15vh', 'margin-top': '20px', 'border-radius': '100px',
                                    'cursor': 'pointer'}),
                    html.P('Paddington and Tom go on a marmalade sandwich adventure...', style={'font-size': '15px','color': 'white', 'font-weight': 'bold', 'line-height':'5vh', 'margin-left':'2vw', 'margin-right':'2vw', 'margin-top':'3vh'})],
                    id='paddington_div',  style={'height':'40vh', 'text-align':'center', 'background-color':'#FFDDAE', 'border-radius':'50px', 'width':'25vw', 'margin-left':'2.5vw', 'margin-right':'10vw'}, className='hover-effect'
                ),
                html.Div([
                    html.Img(id='paddington_story2',
                             src='assets/pictures/paddington.webp',
                             style={'height': '15vh', 'margin-top': '20px', 'border-radius': '100px',
                                    'cursor': 'pointer'}),
                    html.Div('Paddington and Tom go on a marmalade sandwich adventure...', style={'font-size': '15px','color': 'white', 'font-weight': 'bold', 'line-height':'5vh', 'margin-left':'2vw', 'margin-right':'2vw', 'margin-top':'3vh'})],
                    id='paddington_div2',  style={'height':'40vh', 'text-align':'center', 'background-color':'#FFDDAE', 'border-radius':'50px', 'width':'25vw'}, className='hover-effect'
                ),
                    html.Div([
                        html.Img(id='paddington_story3',
                                 src='assets/pictures/paddington.webp',
                                 style={'height': '15vh', 'margin-top': '20px', 'border-radius': '100px',
                                        'cursor': 'pointer'}),
                        html.P('Paddington and Tom go on a marmalade sandwich adventure...',
                               style={'font-size': '15px','color': 'white', 'font-weight': 'bold', 'line-height':'5vh', 'margin-left':'2vw', 'margin-right':'2vw', 'margin-top':'3vh'})],
                        id='paddington_div3',
                        style={'height': '40vh', 'text-align': 'center', 'background-color': '#FFDDAE',
                               'border-radius': '50px', 'width': '25vw', 'margin-left': '10vw', 'margin-right': '2.5vw'}, className='hover-effect'
                    )
                ], style={'display':'flex'}),


                # Audio component
                html.Audio(id='test', controls=True, muted=False, autoPlay=True, style={'display': 'none'})
            ], style={'width': '100%', 'border-radius': '100px'})
        )
    ], style = {'display':'flex'}
    )
    ], style={'background-color': '#FAF9F6',
    # 'background-image': 'url("assets/pictures/background.avif")',  # Replace with your image path
    'background-size': 'cover',  # Ensures the image covers the entire background
    'background-position': 'center',  # Centers the image
    'background-repeat': 'no-repeat',  # Prevents tiling
    'height': '100vh'})




@app.callback(
    Output("story_store", "data"),
    Output("test", "hidden"),
    # Output("test", "autoPlay"),
    Output('narrator-modal', 'is_open'),
    Input("peppa_pig_story", "n_clicks"),
    Input("postman_pat_story", "n_clicks"),
    Input("bowser_story", "n_clicks"),
    Input("paddington_story", "n_clicks"),

)
def play_audio(n_clicks, n_clicks_pat, n_clicks_bowser, n_clicks_paddington):
    triggered_story = ctx.triggered_id
    if (n_clicks is None) & (n_clicks_pat is None) & (n_clicks_bowser is None) & (n_clicks_paddington is None):
        raise PreventUpdate
    elif ctx.triggered_id == 'postman_pat_story':
        print('this one')
        return "/assets/audio/postman_pat.mp3", True, True
    elif ctx.triggered_id == 'peppa_pig_story':  # Trigger playback only when button is clicked
        return "/assets/audio/peppa_pig_linesman.mp3", True, True  # Path to your audio file in assets folder
    elif ctx.triggered_id == 'bowser_story':  # Trigger playback only when button is clicked
        return "/assets/audio/bowser_story.mp3", True, True  # Path to your audio file in assets folder
    elif ctx.triggered_id == 'paddington_story':  # Trigger playback only when button is clicked
        return "/assets/audio/paddington.mp3", True, True  # Path to your audio file in assets folder

    else:
        return "/assets/audio/peppa_pig_linesman.mp3", True, False  # No audio initially


@app.callback(Output("test", "autoPlay", allow_duplicate=True),
                     Output("test", "src"),
              Output('narrator-modal', 'is_open', allow_duplicate=True),
              Input('liam', 'n_clicks'),
              Input("story_store", "data"),
              prevent_initial_call=True
              )

def play_narrators_audio(n_clicks_liam, story):
    if n_clicks_liam is None:
        print('first one')
        raise PreventUpdate
    elif ctx.triggered_id == 'liam':
        print('yes true')
        return True, story, False
    else:
        print('last one')
        raise PreventUpdate

# Use os to get port if available, otherwise default to 8000
if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
else:
    port = 8000

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=port, debug=True)
