Ml_deployement-parent folder
    -model/(stores the models)
        .pkl(model files)
    -templates/(stores the templates)
        -home.html(to render the form)
    -main.py(logic file)

pip install -r requirements.txt
pip freeze >requirements.txt

conda env commands

-create  a venv-- conda create -n <diabetic_env> python==3.7
-to check all the libraries present 