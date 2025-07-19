require 'sinatra'
require 'yaml'

get '/load' do
  data = params[:data]  # ?data=--- !ruby/hash:Kernel {system: ['ls']}
  begin
    YAML.load(data).to_s
  rescue => e
    "Error: #{e}"
  end
end
