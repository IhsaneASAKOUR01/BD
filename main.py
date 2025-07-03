import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

st.set_page_config(
    page_title="AO Tools Dashboard",
    page_icon="📄",
    layout="wide"
)

# === STYLES ===
st.markdown("""
    <style>
    /* Root sizing */
    html {
        font-size: 13px !important;
        zoom: 0.85;
    }
    
    body, .stApp {
        font-size: 13px;
    }
    
    /* Container width and spacing */
    .main .block-container {
        max-width: 900px;
        padding-left: 1rem;
        padding-right: 1rem;
        margin: auto;
    }
    
    /* Sidebar size + border */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
        width: 300px;
        min-width: 300px;
        border-right: 2px solid #dee2e6;
    }
    
    /* Logo */
    [data-testid="stSidebar"] img {
        display: block;
        width: 180px;
        margin-left: 2rem;
        margin-right: auto;
        margin-top: 1rem;
        margin-bottom: 30px;
    }
    
    /* Title */
    .centered-title {
        text-align: center;
        font-size: 4rem;
        font-weight: 800;
        color: #1d3557;
        margin-bottom: 0.2rem;
        font-family: 'Comic Neue', cursive;
    }
    .subtitle {
        text-align: center;
        color: #6c757d;
        margin-bottom: 2rem;
        font-size: 1rem;
    }
    
    /* Radio buttons */
    .stRadio div[role=radiogroup] > label {
        background: #fff;
        padding: 0.5rem 1rem;
        border: 1px solid #ddd;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        transition: all 0.2s ease-in-out;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .stRadio div[role=radiogroup] > label:hover {
        background-color: #eaf4ff;
        border: 1px solid #339af0;
        cursor: pointer;
    }
    .stRadio input[type="radio"] + div svg {
        fill: #339af0 !important;
    }
    .stRadio div[role=radiogroup] > label:has(input[type="radio"]:checked) {
        background-color: #eaf4ff;
        border: 1px solid #339af0;
        box-shadow: 0 0 4px rgba(51, 154, 240, 0.5);
        font-weight: 600;
        color: #222;
    }
    </style>

""", unsafe_allow_html=True)

# === SIDEBAR ===
with st.sidebar:
    st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIALwAyAMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAAAQQCAwUGB//EADkQAAEEAgECBAMFBgUFAAAAAAEAAgMEBRESBiETMVFhFEGhFSJxgZEWMjNCUrEHI2KD0SRDRHKj/8QAGAEBAQEBAQAAAAAAAAAAAAAAAAECAwT/xAAkEQEBAAIABQQDAQAAAAAAAAAAAQIREhMhMUEDBBRRMmGhIv/aAAwDAQACEQMRAD8A+4oiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICLHfZc61malWQske48TpzgwkNPuVZLeyXKTu6aLWyVkjQ5jw4eoKy5e4UOKMkWO/dSipREQEVDJ5ejiYmy5K1FXjceLXSHWyrbJGyMa9jttcAWuHzCDYi5v21S+1Psxs/K5rZY1hIb233IGh+a6KCUVarcgtumbXmbIYJDFKB/K4eYP6hWEEoiICIiAiIgIiICIiAo+XmipZSSRlUth34jyGN9iTraTqlulOazPkJn1qDvDhY7Utj3/pb7+q6EVKvHX8ARN8IjRaRvf47U0qsdSvHDEBxaPP1KsLVy8RzmHmuU/BUnDQ8Vg9GSuH9itTOn44v4Nu2z/c2u1oJoJx5fZycPpTY/wCBrf8AWWARv99w0rQPJoLTseqp5es6zSfHH2eO7R66W+s8SwNezyIU/ay9eFYRR+aq5C9Hj8fYuWDqKCMvdv0A2o6PB9UUv2v6tkxHI/C42m5zyHf954+6D9D+RXZ/w5ycl3pdkMpBt0XGtI13Yhzew39F57o/p3LZKhJnW5yzj5snK6Z0cUbXbGzrZK3dOQ2OluvZ8XbsvsRZWLxmTOaG8pBsn29fotXXZjq6fSLso7P5w2K1RrXWx4zo5nEtPhjWu3cfjrzVvBdR5POytdUx0MdSOZ8ViaWU+YJGmDXc61+q29Md811J7XWj/wCbU6BA/Z5uvM2bGz/uuUqzaxjcvW8HM2ZYo60VK3I2V7f5+LWnmfc7+iqQ5XqW5VF+njKbazhyjrzzFs0jfl8uLT+K5NmtPc6c6ygrgySm/KWtaO7tNYdfReqx+WoWsTFfisRNrGMOLi4AM9QfRUVP2nhPTrMvHBK9z9NbX1p5kJ1x/X5qpezWfxNX7QydKiaTS3xWwSuMkbSQN9xo+a15PqOaXCULVJnwjb9wQsmnaCI2EnUmvfXbfquT13QhqdN2X3s5kLU5aBHC6YBr3bH8jQN/mobfRA4EAj5qVphO4mcSCNDRW1RpKIiAiIgIiIIVa6ZRXc6uOUje4BCtaUEJOlSzcVadtlqHm3YcPNp8wVaXJAuQ35jHUa6N+uL+eh77C3mO+92/io2N/pZFv6krVjEzs7r+1K59O1K6xLWs8RJGA4Fvk5p+avhSzTcu0aCqkCrIT5RyHv8A6Xf8K2tb+PE8z93Xfak+ksZbWm3Wr3Kz69uNssLxpzHjYIXKqxOyNw2OcjajTpjOZ1J769Ffykpq4yzLH2McbiNeoC1w9dMT1Lw3LTnS5ylReKFCtLOYQG+HWj2GD0KxrXcXl78PxVTw71f70IsR6c3/ANVs6RrRw4aB4aPEmHN7vmSfVXLuLr3J4LL+TJYDtrm9j+B9lvLgl4XLDm3GZ/xMElCK7ajh4NsHUk4aO57aBP5BZYo03U2ux3AVySW8RodySfquTXIHVOS0P/HYtAzk8HTtW7HBE18knExtaePmfL9E5V8JPcSXq9LDVrwGQwxMYZXl7+I/ecRrf0XNl6WwU1l1iTF1zI48nfd7E+pHkufdy2Yxxglsw13xzPDBEzfIOPl3W77SylO7VjyAruhsv4AxA7Yde6crJr5OG9O1ZpVLVZ1azXikgcADG5oLdDy7KhX6awlVkjYcbXAkYWP23ltvp3+SwuW8nLfdVoxsiiYwOdYmaSCT8gtWPyN+xNcpSiv8XAAWvbstdv1CzMLrbV9bHenVx8VWCq2Ck1jYWdmtYdhqtLyHTNmanjbdi0Yvh45HuPEHly3/AGVoX84+r8cI6wh1zEHfnx1vz9VrL0bxaYx9zLj1emRVMbcbfow2mdmyNB16K13XK9Hpl3NxKIiKIiICIiDHQUqUQVnxRNlbO7QeBrl7LeO47H81RylgQwsBbz8V4YB7lWqsbooGMcdkeZV8MS/602FczKudPJFRiOjL/EI+TAumVyqEjHGe9M4Na9/FpcdaaOyuP2z6l8OnFEyJjWMaA1o0B6LVcrizWlgd+69hafzW8HY2FBIALiew8ypvrtu4yzTyeHyzcND9nZcOhdGSGSFp4vb7Lc7Iz5rKVo8a6VtSF3KaYAgP/wBIVB/V1rKSzfYXTsuTqxPLDYdI1jHkefHfmur0x1JWzL7FT4SSleq68arLrk0evbzC63Ob3rq82PpZScO+jGIEdT5JxB0a7O/uuS1pPSWNHE7FgdvnrkV7jQB3rufM6WDw1kTiG9mjeteSc0vt9+XE6oBMeNDQSBdj32327qOpdm1iNAkC2N+y6GFvszGKrXxFwZMzkGE7LVfcAdbAPp22szPWm76O+K776/jx9qaCTN2481YliiZrwIw4ta5uvPt7rLp6StHm7TIGOiimjaYQ8H/MA33G16G7ap1pq0VnQksSeHDtu9u0Tr6JJYe3KQVhTe6N8TnOsgfdYRrTT+Oytc2a05/Gu5d9nmqMfxWDyONYT8UHvd4ZBGxtaon4NuPY6TxxZa3ToPEfyLvTS9sGMaS4AbPmQFj4EXPn4bef9Wu6vO8HxvKphYBBjYWCHwdN34fLlx331tX0/FSfLt5rjbu9Xqxx4ZqJRY78td/wWSjQiIgIiICIiChlITNV2B96NzXt99d1aieJGBzD91w2CsiAVz673Vrfwp2YnN5xO/u1a7xjtltuydo1KrpGjk/YawepKpzQR2bdaq+PUUcfiuZ8ifID+6wsssZO1FGI3RwQycnOf2LvwXZDG75a7+qv4xjVzv6SAANDyWuxF40EkRcWiRpbseY2tyqZKCS1j7NeGV0UkkZayRp7tJHYrDs8BhZ+pOjKbcZPgnZGhC9xjsVHfe0Tvu317rt9MZfAZvNWblSCavlxEGTMsNLH8O3y8vRc3DdXzYSk3HdVUr7bsBLPHZEZWzDZ0QR7LPBRWs71seom4+ajRjreCx07eD53b8yPTv8ARaZi7jWXeqRNkZMnaqUTK9lSGo4MJa0kc3EjezryVnE27tbJ5DB35zaMVcWK87wA58Z2CHa7bBGlTwl0dLwSYnKQ2GQwyvdWsMhdIyRjiXD93ej3Ks4iOxksxkM5JWkggdWFarHKNPe0EkuI+WyRoIOZRt2KXQmAfVlMbpLUETiPm10miF6fquzNT6byVmq8xzRV3PY8fIgea8y2hdP+HuLEdaR1ipLFYMGtOIZJsjXrpbOquoPtbp2/Tw1O5ZsSQlr2mu9nht13J2PP5Aeqnk8HUlSa3f6Zl+0bkTp5Q3URbpp8NxLhtvn+PZdeSzZr9VYuh48joHUpnSctffc0s04/qVR6hc6mzpu5NFKYas4M5Yxzi0GMjuB381ala+z1firkMchrnHz/AOZwI0S6MgHt2PsqKmPbd6nlsXZMlaqUGTvhrQ1HBhcGnRe4635gqxibd2jlreEvWnWuFcWath4AeWbIIdoaJBH1VXE3m9L/ABONykVhtYTvlq2Y4XPY9j3ctHiOxBOlvxbLGUzVzOPgkhr/AAfwtVkreLpBvkX6+QJ7BBU6ZqZXO4GrfyecvxSSNPhtqubGPMgF3b7xP6LNmaysPR2Vm2JshQllg8Vse+fFwHPiPY717Lq9EQyQdLY6Kdjo5Gx6cwjRHc+a5uObkqeKzktCqH3PtGaSOKVmvEbyG9fiN6UGqrXsTVI73T3U1jIWhxcY552ujlHzBaAOPzXtGlxaOQ0fmF88zcmGydJ/2TirMOcd/B8Oo+KSN/b95wGtevde+qiVtaJs7tyhg5keXLXdKRvREUaEREBERBCxLGkgkdx5LNETTHSlSiKIiII0E0FKII4j0TiPRSiCOI3vScRrRClEEaCcQpRBHEJxG96UogjQQNAUogjiPRAAPJSiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIg//2Q==")
    choice = st.radio("Choose a tool22", [
        "CVs & REFs Adapter",
        "Reference Creator",
        "CVs Extractor & Mapper"
    ])

# === HEADER ===
st.markdown("<div class='centered-title'>BD Tools Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart automation tools for project references & resumes</div>", unsafe_allow_html=True)
st.markdown("---")

# === MAIN ===
if choice == "CVs & REFs Adapter":
    st.subheader("CVs & REFs Adapter")
    st.write("Extract, align and enhance CVs & reference docs per AO instructions.")
    run_cvs_refs_adapter()

elif choice == "Reference Creator":
    st.subheader("Reference Creator")
    st.write("Generate complete bilingual references directly from reports.")
    run_ref_creator()

else:
    st.subheader("CVs Extractor & Mapper")
    st.write("Extract, map, and reformat CVs into your preferred structure.")
    run_cvs_adapter()
