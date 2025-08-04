require 'sinatra'
require 'yaml'

get '/load' do
  data = params[:data] 
  begin
    YAML.load(data).to_s
  rescue => e
    "Error: #{e}"
  end
end
